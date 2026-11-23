#!/usr/bin/env python3
"""
find_cyberleek_gateways.py

Finds working Arweave gateways for the Cyberleek site and returns only safe ones.

This script is specifically configured for the "cyberleek" ArNS name and cannot
be used for other sites.

Usage:
    python find_cyberleek_gateways.py [options]

Examples:
    python find_cyberleek_gateways.py
    python find_cyberleek_gateways.py --top 5
    python find_cyberleek_gateways.py --format url
    python find_cyberleek_gateways.py --output safe_gateways.json
"""

import argparse
import json
import socket
import ssl
import sys
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from typing import Optional


# ---------------------------------------------------------------------------
# HARDCODED TARGET - This script only works for Cyberleek
# ---------------------------------------------------------------------------
CYBERLEEK_TARGET = "cyberleek"


# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

BOOTSTRAP_NODES = [
    "ardrive.net",
    "arweave.net",
    "permaweb.io",
    "arns.app",
]

DEFAULT_WORKERS = 20
DEFAULT_TIMEOUT = 10
DEFAULT_MIN_SCORE = 2


# ---------------------------------------------------------------------------
# Data model
# ---------------------------------------------------------------------------

@dataclass
class SafeGateway:
    hostname: str
    url: str
    latency_ms: int
    safety_score: int
    ssl_valid: bool
    is_ario_node: bool
    in_registry: bool
    operator_stake: Optional[int]
    registry_status: Optional[str]


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _ssl_context() -> ssl.SSLContext:
    return ssl.create_default_context()


def _get(url: str, timeout: int, full_body: bool = False) -> tuple[int, bytes]:
    """GET url and return (status, body). Raises on error."""
    headers = {"User-Agent": "cyberleek-gateway-finder/1.0", "Accept": "application/json"}
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=timeout, context=_ssl_context()) as r:
        body = r.read() if full_body else r.read(512)
        return r.status, body


# ---------------------------------------------------------------------------
# Gateway discovery
# ---------------------------------------------------------------------------

def fetch_gateway_list(timeout: int = 12) -> list[str]:
    """
    Fetch live gateway list from AR.IO network via /ar-io/peers endpoint.
    """
    for node in BOOTSTRAP_NODES:
        try:
            url = f"https://{node}/ar-io/peers"
            _, body = _get(url, timeout, full_body=True)
            data = json.loads(body.decode("utf-8"))
            
            fqdns: list[str] = []
            for key, entry in data.get("gateways", {}).items():
                raw_url = entry.get("url", "")
                if raw_url.startswith("https://"):
                    fqdn = raw_url.replace("https://", "").split("/")[0].split(":")[0]
                else:
                    fqdn = key.split(":")[0]
                if fqdn:
                    fqdns.append(fqdn.lower())
            
            if fqdns:
                seen = set()
                unique = []
                for f in [node] + fqdns:
                    if f not in seen:
                        seen.add(f)
                        unique.append(f)
                
                print(f"[+] Discovered {len(unique)} gateways from {node}/ar-io/peers", file=sys.stderr)
                return unique
                
        except Exception as exc:
            print(f"[!] Bootstrap {node} failed: {exc}", file=sys.stderr)
    
    # Hardcoded fallback
    print("[!] Using fallback gateway list", file=sys.stderr)
    return [
        "arweave.net", "ar-io.dev", "ardrive.net", "permaweb.io",
        "arns.app", "g8way.io", "ar.io", "arweave.dev",
    ]


# ---------------------------------------------------------------------------
# Step 1: Test gateway availability for Cyberleek
# ---------------------------------------------------------------------------

def test_gateway_availability(fqdn: str, timeout: int) -> Optional[tuple[str, int]]:
    """
    Test if gateway can serve Cyberleek content.
    Returns (url, latency_ms) if successful, None otherwise.
    """
    candidates = [
        f"https://{CYBERLEEK_TARGET}.{fqdn}",
        f"https://{fqdn}/{CYBERLEEK_TARGET}",
    ]
    
    for url in candidates:
        t0 = time.monotonic()
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "cyberleek-gateway-finder/1.0"})
            with urllib.request.urlopen(req, timeout=timeout, context=_ssl_context()) as resp:
                if resp.status == 200:
                    latency = round((time.monotonic() - t0) * 1000)
                    return (url, latency)
        except:
            pass
    
    return None


# ---------------------------------------------------------------------------
# Step 2: Verify gateway safety
# ---------------------------------------------------------------------------

def check_ssl(hostname: str) -> bool:
    """Quick SSL certificate validation."""
    try:
        ctx = ssl.create_default_context()
        with socket.create_connection((hostname, 443), timeout=8) as sock:
            with ctx.wrap_socket(sock, server_hostname=hostname) as ssock:
                ssock.getpeercert()
                return True
    except:
        return False


def check_ario_node(hostname: str) -> bool:
    """Check if gateway is an AR.IO node."""
    try:
        url = f"https://{hostname}/ar-io/info"
        status, body = _get(url, 8)
        data = json.loads(body.decode("utf-8"))
        return "wallet" in data and "programIds" in data
    except:
        return False


def check_registry(hostname: str, registry_data: dict) -> tuple[bool, Optional[int], Optional[str]]:
    """Check if gateway is in the registry."""
    gateways = registry_data.get("gateways", {})
    for key, entry in gateways.items():
        entry_host = key.split(":")[0].lower()
        entry_url = entry.get("url", "")
        
        if hostname.lower() in (entry_host, entry_url.replace("https://", "").split("/")[0].lower()):
            return (
                True,
                entry.get("operatorStake"),
                entry.get("status"),
            )
    
    return (False, None, None)


def verify_gateway_safety(
    hostname: str,
    url: str,
    latency_ms: int,
    registry_data: dict,
) -> SafeGateway:
    """Run all safety checks and compute safety score."""
    ssl_valid = check_ssl(hostname)
    is_ario = check_ario_node(hostname)
    in_reg, stake, status = check_registry(hostname, registry_data)
    accessible = True
    
    score = sum([ssl_valid, is_ario, in_reg, accessible])
    
    return SafeGateway(
        hostname=hostname,
        url=url,
        latency_ms=latency_ms,
        safety_score=score,
        ssl_valid=ssl_valid,
        is_ario_node=is_ario,
        in_registry=in_reg,
        operator_stake=stake,
        registry_status=status,
    )


# ---------------------------------------------------------------------------
# Main pipeline
# ---------------------------------------------------------------------------

def find_safe_gateways(
    workers: int = DEFAULT_WORKERS,
    timeout: int = DEFAULT_TIMEOUT,
    min_score: int = DEFAULT_MIN_SCORE,
    top_n: Optional[int] = None,
) -> list[SafeGateway]:
    """Find safe gateways for Cyberleek."""
    
    print(f"[*] Finding safe gateways for '{CYBERLEEK_TARGET}'...\n", file=sys.stderr)
    
    # Discover gateways
    all_gateways = fetch_gateway_list()
    total = len(all_gateways)
    
    # Fetch registry data once
    registry_data = {}
    try:
        url = f"https://{BOOTSTRAP_NODES[0]}/ar-io/peers"
        _, body = _get(url, 15, full_body=True)
        registry_data = json.loads(body.decode("utf-8"))
    except:
        pass
    
    # Test availability in parallel
    print(f"[*] Testing {total} gateways for Cyberleek availability...", file=sys.stderr)
    working = []
    done = 0
    
    with ThreadPoolExecutor(max_workers=workers) as pool:
        futures = {
            pool.submit(test_gateway_availability, fqdn, timeout): fqdn
            for fqdn in all_gateways
        }
        
        for future in as_completed(futures):
            done += 1
            result = future.result()
            if result:
                url, latency = result
                hostname = futures[future]
                working.append((hostname, url, latency))
                print(f"  [{done:>3}/{total}] {hostname:<40} OK  {latency:>5} ms", file=sys.stderr)
    
    if not working:
        print("\n[!] No working gateways found for Cyberleek.", file=sys.stderr)
        return []
    
    print(f"\n[*] Found {len(working)} working gateways", file=sys.stderr)
    print(f"[*] Verifying safety...\n", file=sys.stderr)
    
    # Verify safety
    safe_gateways = []
    for idx, (hostname, url, latency) in enumerate(working, 1):
        print(f"  [{idx:>3}/{len(working)}] Checking {hostname}...", file=sys.stderr)
        gateway = verify_gateway_safety(hostname, url, latency, registry_data)
        
        if gateway.safety_score >= min_score:
            safe_gateways.append(gateway)
            status = "SAFE" if gateway.safety_score >= 3 else "USABLE"
            print(f"           {status} - Score: {gateway.safety_score}/4", file=sys.stderr)
        else:
            print(f"           UNSAFE - Score: {gateway.safety_score}/4 (filtered)", file=sys.stderr)
    
    # Sort by score, stake, latency
    safe_gateways.sort(
        key=lambda g: (
            -g.safety_score,
            -(g.operator_stake or 0),
            g.latency_ms,
        )
    )
    
    if top_n:
        safe_gateways = safe_gateways[:top_n]
    
    return safe_gateways


# ---------------------------------------------------------------------------
# Output formatting
# ---------------------------------------------------------------------------

def print_results(gateways: list[SafeGateway], format_type: str) -> None:
    """Print results in requested format."""
    
    if not gateways:
        print("\n[!] No safe gateways found meeting the minimum score requirement.", file=sys.stderr)
        return
    
    if format_type == "url":
        for g in gateways:
            print(g.url)
    
    elif format_type == "hostname":
        for g in gateways:
            print(g.hostname)
    
    elif format_type == "table":
        print("\n" + "="*90, file=sys.stderr)
        print(f"  SAFE GATEWAYS FOR {CYBERLEEK_TARGET.upper()}", file=sys.stderr)
        print("="*90, file=sys.stderr)
        print(f"  {'Gateway':<40} {'Score':<8} {'Latency':<10} {'Stake (ARIO)':<15}", file=sys.stderr)
        print("-"*90, file=sys.stderr)
        
        for g in gateways:
            stake_ario = (g.operator_stake or 0) / 1_000_000
            status_icon = "[OK]" if g.safety_score >= 3 else "[!!]"
            print(
                f"  {status_icon} {g.hostname:<37} {g.safety_score}/4      "
                f"{g.latency_ms:>5} ms   {stake_ario:>12,.0f}",
                file=sys.stderr
            )
        
        print("="*90 + "\n", file=sys.stderr)
        print(f"Found {len(gateways)} safe gateways for Cyberleek.", file=sys.stderr)
        print(f"\nFastest: {gateways[0].url}", file=sys.stderr)
    
    elif format_type == "json":
        output = [
            {
                "hostname": g.hostname,
                "url": g.url,
                "latency_ms": g.latency_ms,
                "safety_score": g.safety_score,
                "ssl_valid": g.ssl_valid,
                "is_ario_node": g.is_ario_node,
                "in_registry": g.in_registry,
                "operator_stake": g.operator_stake,
                "registry_status": g.registry_status,
            }
            for g in gateways
        ]
        print(json.dumps(output, indent=2))


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description=f"Find working Arweave gateways for {CYBERLEEK_TARGET} and return only the safe ones.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        "--min-score",
        type=int,
        default=DEFAULT_MIN_SCORE,
        choices=[0, 1, 2, 3, 4],
        help=f"Minimum safety score 0-4 (default: {DEFAULT_MIN_SCORE})",
    )
    parser.add_argument(
        "--top",
        type=int,
        metavar="N",
        help="Return only top N gateways",
    )
    parser.add_argument(
        "--workers",
        type=int,
        default=DEFAULT_WORKERS,
        help=f"Parallel threads (default: {DEFAULT_WORKERS})",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=DEFAULT_TIMEOUT,
        help=f"Timeout per gateway in seconds (default: {DEFAULT_TIMEOUT})",
    )
    parser.add_argument(
        "--format",
        choices=["table", "url", "hostname", "json"],
        default="table",
        help="Output format (default: table)",
    )
    parser.add_argument(
        "--output",
        metavar="FILE",
        help="Save JSON results to file",
    )
    
    args = parser.parse_args()
    
    # Find safe gateways for Cyberleek
    gateways = find_safe_gateways(
        workers=args.workers,
        timeout=args.timeout,
        min_score=args.min_score,
        top_n=args.top,
    )
    
    # Save to file if requested
    if args.output:
        output = [
            {
                "hostname": g.hostname,
                "url": g.url,
                "latency_ms": g.latency_ms,
                "safety_score": g.safety_score,
                "ssl_valid": g.ssl_valid,
                "is_ario_node": g.is_ario_node,
                "in_registry": g.in_registry,
                "operator_stake": g.operator_stake,
                "registry_status": g.registry_status,
            }
            for g in gateways
        ]
        with open(args.output, "w") as f:
            json.dump(output, f, indent=2)
        print(f"[+] Results saved to {args.output}\n", file=sys.stderr)
    
    # Print results
    print_results(gateways, args.format)
    
    sys.exit(0 if gateways else 1)


if __name__ == "__main__":
    main()
