# Cyberleek Gateway Finder

Find working Arweave gateways for Cyberleek.

## 🚀 Quick Start (No Installation)

### Option 1: Google Colab (Easiest - runs in your browser)

**One-click method:**
1. Go to [Google Colab](https://colab.research.google.com/)
2. Click **File → New notebook**
3. Paste this code and click **Run** ▶️:

```python
!wget -q https://raw.githubusercontent.com/YOUR_USERNAME/cyberleek-gateway-finder/main/find_cyberleek_gateways.py
!python find_cyberleek_gateways.py --top 10 --format url
```

4. Wait 30-60 seconds for results!

### Option 2: Replit (Also Easy)

1. Go to [Replit](https://replit.com/)
2. Click **+ Create Repl**
3. Choose **Python**
4. Paste this in the editor and click **Run**:

```python
import urllib.request
import sys

# Download the script
url = 'https://raw.githubusercontent.com/YOUR_USERNAME/cyberleek-gateway-finder/main/find_cyberleek_gateways.py'
script = urllib.request.urlopen(url).read().decode('utf-8')

# Execute it
exec(script)
```

### Option 3: Jupyter Notebook (Online)

1. Go to [Jupyter.org Try](https://jupyter.org/try-jupyter/lab/)
2. Create a new Python 3 notebook
3. Paste and run:

```python
!wget https://raw.githubusercontent.com/YOUR_USERNAME/cyberleek-gateway-finder/main/find_cyberleek_gateways.py
!python find_cyberleek_gateways.py --format url
```

---

## 💻 Local Installation (For Technical Users)

### Requirements
- Python 3.8+ (no external dependencies)

### Usage

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

---

## 🔧 How It Works

1. Discovers 300+ gateways from the AR.IO network
2. Tests which ones can serve Cyberleek
3. Verifies SSL, AR.IO node status, and registry membership
4. Returns only safe gateways sorted by speed

## ⚠️ Disclaimer

**This tool only finds gateways. I am not responsible for what you do on Cyberleek or any content you access through these gateways. Use at your own risk.**

The gateways returned by this script are third-party services operated by independent node operators. I do not control, endorse, or take responsibility for:
- The content hosted on Cyberleek
- The gateways or their operators
- Your use of these gateways
- Any actions you take after accessing Cyberleek

By using this tool, you acknowledge that you are solely responsible for your own actions and any consequences thereof.

## 💰 Support

If you find this tool useful, consider supporting development:

**Bitcoin (BTC):** `bc1q7wlprmc20rdjyqjsghkhtnmndjs4dpmq26sz6h`

## 📄 License

MIT License - See LICENSE file for details
