# Cyberleek Gateway Finder

Find working and safe Arweave gateways for the Cyberleek site.

This tool discovers live gateways from the AR.IO network, tests which ones can serve Cyberleek content, and verifies their safety through SSL checks, AR.IO node validation, and registry membership verification.

## Features

- 🔍 Discovers 300+ gateways from the AR.IO Gateway Address Registry
- ⚡ Parallel testing for speed
- 🛡️ Safety verification (SSL, AR.IO node, registry membership, stake)
- 📊 Multiple output formats (table, URL list, hostname list, JSON)
- 🎯 Hardcoded for Cyberleek — cannot be used for other sites

## Quick Start

```bash
# Find safe Cyberleek gateways
python find_cyberleek_gateways.py

# Get top 5 as URLs only
python find_cyberleek_gateways.py --top 5 --format url

# Save to JSON
python find_cyberleek_gateways.py --output safe_gateways.json

# Adjust safety requirements
python find_cyberleek_gateways.py --min-score 3
```

## Requirements

- Python 3.8+ (no external dependencies)

## Usage

```
python find_cyberleek_gateways.py [options]

Options:
  --min-score {0,1,2,3,4}  Minimum safety score (default: 2)
  --top N                  Return only top N gateways
  --workers N              Parallel threads (default: 20)
  --timeout N              Timeout per gateway in seconds (default: 10)
  --format {table,url,hostname,json}
                           Output format (default: table)
  --output FILE            Save JSON results to file
```

## Safety Scoring

Each gateway is scored 0-4 based on:

| Check | Description |
|-------|-------------|
| ✓ SSL Valid | Valid certificate from trusted CA |
| ✓ AR.IO Node | Runs AR.IO gateway software |
| ✓ In Registry | Registered with economic stake |
| ✓ Accessible | Successfully serves Cyberleek content |

**Score interpretation:**
- **4/4 or 3/4** = SAFE — Recommended
- **2/4** = USABLE — Use with caution
- **1/4 or 0/4** = UNSAFE — Filtered out (unless `--min-score 0`)

## Output Formats

### Table (default)
```
==========================================================================================
  SAFE GATEWAYS FOR CYBERLEEK
==========================================================================================
  Gateway                                  Score    Latency    Stake (ARIO)
------------------------------------------------------------------------------------------
  [OK] ar9.nangluong.store                   4/4        203 ms         35,877
  [OK] aoweave.tech                          3/4        281 ms         15,000
==========================================================================================
```

### URL List
```bash
python find_cyberleek_gateways.py --format url
```
```
https://cyberleek.ar9.nangluong.store
https://cyberleek.aoweave.tech
https://cyberleek.ardrive.net
```

### Hostname List
```bash
python find_cyberleek_gateways.py --format hostname
```
```
ar9.nangluong.store
aoweave.tech
ardrive.net
```

### JSON
```bash
python find_cyberleek_gateways.py --format json
```
```json
[
  {
    "hostname": "ar9.nangluong.store",
    "url": "https://cyberleek.ar9.nangluong.store",
    "latency_ms": 203,
    "safety_score": 4,
    "ssl_valid": true,
    "is_ario_node": true,
    "in_registry": true,
    "operator_stake": 35877000000,
    "registry_status": "joined"
  }
]
```

## Examples

**Get the fastest safe gateway:**
```bash
python find_cyberleek_gateways.py --top 1 --format url
```

**Find only the safest gateways (score 3+):**
```bash
python find_cyberleek_gateways.py --min-score 3
```

**Quick check with fewer threads:**
```bash
python find_cyberleek_gateways.py --workers 10 --timeout 5
```

**Export for automation:**
```bash
python find_cyberleek_gateways.py --format url > cyberleek_gateways.txt
```

## How It Works

1. **Discovery** — Fetches the live Gateway Address Registry by calling `/ar-io/peers` on a bootstrap node
2. **Availability Testing** — Tests all gateways in parallel to see which ones can serve Cyberleek
3. **Safety Verification** — Checks SSL certificates, AR.IO node identity, and registry membership
4. **Filtering & Sorting** — Returns only gateways meeting the minimum safety score, sorted by score → stake → latency

## Security Notes

- Gateways with 4/4 score have valid SSL, run AR.IO software, and have economic stake
- Economic stake is typically 20,000+ ARIO tokens (~$40 USD at current prices)
- Stake is NOT a strong deterrent — the real security is Arweave's content addressing
- **Always verify content integrity** when accessing sensitive data
- Use multiple gateways and compare content hashes for important operations

## Why Cyberleek-Only?

This script is hardcoded to only work with the "cyberleek" ArNS name. This is by design — it's a focused tool for finding Cyberleek mirrors, not a general-purpose gateway finder.

If you need to find gateways for other sites, see the general-purpose tools in the [arweave-gateway-tools](../arweave-gateway-tools) directory.

## License

MIT License

## Credits

Based on the [AR.IO Gateway Architecture](https://docs.ar.io/learn/gateways/) and inspired by [CyberleekWebsiteMirrorFinder](https://github.com/divinityAPE/CyberleekWebsiteMirrorFinder).
