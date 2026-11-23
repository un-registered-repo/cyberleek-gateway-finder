# Cyberleek Gateway Finder

Find working Arweave gateways for Cyberleek.

## Usage

```bash
python find_cyberleek_gateways.py
```

That's it. The script finds safe gateways and shows them in a table.

### Options

```bash
# Get just URLs
python find_cyberleek_gateways.py --format url

# Get top 5 fastest
python find_cyberleek_gateways.py --top 5

# Save to JSON
python find_cyberleek_gateways.py --output gateways.json

# Adjust safety requirements (0-4, default 2)
python find_cyberleek_gateways.py --min-score 3
```

## Requirements

Python 3.8+ (no external dependencies)

## How It Works

1. Discovers 300+ gateways from the AR.IO network
2. Tests which ones can serve Cyberleek
3. Verifies SSL, AR.IO node status, and registry membership
4. Returns only safe gateways sorted by speed

## Disclaimer

**This tool only finds gateways. I am not responsible for what you do on Cyberleek or any content you access through these gateways. Use at your own risk.**

The gateways returned by this script are third-party services operated by independent node operators. I do not control, endorse, or take responsibility for:
- The content hosted on Cyberleek
- The gateways or their operators
- Your use of these gateways
- Any actions you take after accessing Cyberleek

By using this tool, you acknowledge that you are solely responsible for your own actions and any consequences thereof.

## Support

If you find this tool useful, consider supporting development:

**Bitcoin (BTC):** `bc1q7wlprmc20rdjyqjsghkhtnmndjs4dpmq26sz6h`

## License

MIT License - See LICENSE file for details
