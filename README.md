# Cyberleek Gateway Finder

Find working Arweave gateways for Cyberleek.

**💰 Bitcoin Donations:** `bc1q7wlprmc20rdjyqjsghkhtnmndjs4dpmq26sz6h`

**⚠️ IMPORTANT DISCLAIMERS:**
- **I have NO affiliation with the Cyberleek project, its creators, or operators**
- This is an independent tool for finding gateway mirrors
- I do not host, create, or control any content on Cyberleek
- I do not endorse or promote any content found through these gateways

## 🚀 Quick Start (No Installation)

### Option 1: Google Colab (Easiest - runs in your browser)

**One-click method:**
1. Go to [Google Colab](https://colab.research.google.com/)
2. Click **File → New notebook**
3. Create a code box with "+ Code" Paste this code and click **Run** ▶️:

```python
import urllib.request
import sys

# Download the script
url = 'https://raw.githubusercontent.com/palexlega/cyberleek-gateway-finder/main/find_cyberleek_gateways.py'
response = urllib.request.urlopen(url)
script_content = response.read().decode('utf-8')

# Save it to a file
with open('find_cyberleek_gateways.py', 'w') as f:
    f.write(script_content)

# Run it with arguments
sys.argv = ['find_cyberleek_gateways.py', '--top', '10', '--format', 'url']
exec(script_content)
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
url = 'https://raw.githubusercontent.com/palexlega/cyberleek-gateway-finder/main/find_cyberleek_gateways.py'
script = urllib.request.urlopen(url).read().decode('utf-8')

# Execute it with default arguments
exec(script)
```

### Option 3: Jupyter Notebook (Online)

1. Go to [Jupyter.org Try](https://jupyter.org/try-jupyter/lab/)
2. Create a new Python 3 notebook
3. Paste and run:

```python
!pip install -q requests 2>/dev/null || true
!wget -q https://raw.githubusercontent.com/palexlega/cyberleek-gateway-finder/main/find_cyberleek_gateways.py -O gateway_finder.py
!python3 gateway_finder.py --format url
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

## 🔧 Using for Other ArNS Names

**This script is hardcoded for "cyberleek" only.** To use it for other Arweave/ArNS sites:

### Method 1: Edit the Script

1. Download `find_cyberleek_gateways.py`
2. Open it in a text editor
3. Find this line near the top:
   ```python
   CYBERLEEK_TARGET = "cyberleek"
   ```
4. Change `"cyberleek"` to your desired ArNS name:
   ```python
   CYBERLEEK_TARGET = "ardrive"  # or any other ArNS name
   ```
5. Save and run the modified script

### Method 2: Use the General Tool

For a tool that works with any ArNS name or transaction ID, see the general-purpose [arweave-gateway-tools](https://github.com/palexlega/arweave-gateway-tools) repository (if available).

---

## 🔧 How It Works

1. Discovers 300+ gateways from the AR.IO network
2. Tests which ones can serve Cyberleek
3. Verifies SSL, AR.IO node status, and registry membership
4. Returns only safe gateways sorted by speed

## ⚠️ Legal Disclaimer

**READ CAREFULLY BEFORE USING THIS TOOL:**

### No Affiliation
- I have **NO affiliation, association, authorization, endorsement, or connection** with:
  - The Cyberleek project, website, or any of its creators/operators
  - Any content hosted on Cyberleek or accessible through these gateways
  - Any ArNS names, Arweave applications, or projects mentioned
- This is an **independent, third-party tool** for technical gateway discovery only

### No Responsibility or Liability
**This tool only finds gateways. I am not responsible for:**
- Any content you access, view, download, or interact with through these gateways
- What you do on Cyberleek or any other site
- The legality, safety, or appropriateness of any content
- Any actions taken by gateway operators
- Any harm, damages, or consequences resulting from your use of this tool
- Any violations of law, terms of service, or third-party rights

### Third-Party Services
The gateways returned by this script are:
- **Operated by independent third parties** (AR.IO node operators)
- **Not controlled, endorsed, or verified by me** beyond technical functionality
- **Subject to their own terms of service and policies**
- **May log your activity, block content, or change availability** at any time

### User Responsibility
By using this tool, you acknowledge and agree that:
- **You are solely responsible** for your actions and their consequences
- **You will comply** with all applicable laws, regulations, and terms of service
- **You will not use** this tool for illegal purposes
- **You assume all risks** associated with accessing content through these gateways
- **You will not hold me liable** for any outcomes related to your use of this tool

### No Warranty
This tool is provided "AS IS" without warranty of any kind, express or implied, including but not limited to:
- Warranties of merchantability or fitness for a particular purpose
- Accuracy, reliability, or availability of results
- Security or privacy of your usage
- Compliance with any laws or regulations

### Jurisdiction
If you are uncertain about the legality of accessing certain content in your jurisdiction, **consult a lawyer before using this tool**. The existence of this tool does not constitute legal advice or permission to access any content.

### Content Policy
I do not:
- Monitor what content exists on Cyberleek or other ArNS sites
- Review, approve, or screen any content accessible through these gateways
- Make any representations about the nature of any content
- Encourage or discourage accessing any particular content

**USE AT YOUR OWN RISK. IF YOU DO NOT AGREE TO THESE TERMS, DO NOT USE THIS TOOL.**

## 💰 Support

If you find this tool useful, Bitcoin donations are appreciated:

**BTC:** `bc1q7wlprmc20rdjyqjsghkhtnmndjs4dpmq26sz6h`

## 📄 License

MIT License - See LICENSE file for details
