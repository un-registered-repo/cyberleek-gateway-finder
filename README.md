# Cyberleek Gateway Finder

**Find working Arweave gateways for Cyberleek - no installation required, runs in your browser.**

A Python tool that discovers and tests 300+ AR.IO gateways to find the fastest, most reliable access points for the Cyberleek ArNS name on the Arweave network.

## ⚠️ WARNING: Beware of Scam Sites

**Posting this repo so people don't fall for fake scam websites that ask for money.** The real Cyberleek website is hosted on Arweave and can only be accessed using an Arweave gateway. **The real website DOES NOT ASK FOR MONEY.**

If a site claiming to be Cyberleek asks for payment, credit cards, or crypto donations to "unlock" content, **it is a scam**. This tool helps you find legitimate Arweave gateways for the authentic Cyberleek ArNS name.
## Support if you found this useful:
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
url = 'https://raw.githubusercontent.com/un-registered-repo/cyberleek-gateway-finder/master/find_cyberleek_gateways.py'
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
url = 'https://raw.githubusercontent.com/un-registered-repo/cyberleek-gateway-finder/master/find_cyberleek_gateways.py'
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
!wget -q https://raw.githubusercontent.com/un-registered-repo/cyberleek-gateway-finder/master/find_cyberleek_gateways.py -O gateway_finder.py
!python3 gateway_finder.py --format url
```
## ❓ Common Problems This Solves

- **"Cyberleek not loading"** - Gateway timeouts or downtime
- **"Arweave gateway down"** - Primary gateway offline
- **"Cannot access ArNS name"** - DNS resolution issues
- **"ar.io gateway timeout"** - Slow or unresponsive gateways
- **"Need Cyberleek mirror"** - Finding alternative access points
- **"Arweave content unavailable"** - Gateway-specific blocking or errors

This tool automatically finds working alternatives when your usual gateway fails.
---

## 💻 Local Installation (For Technical Users)

### Requirements
- Python 3.8+ (no external dependencies - uses standard library only)
- Works on Windows, macOS, and Linux

### Installation

No installation needed - it's a single self-contained Python script:

```bash
# Download the script
wget https://raw.githubusercontent.com/un-registered-repo/cyberleek-gateway-finder/master/find_cyberleek_gateways.py

# Or using curl
curl -O https://raw.githubusercontent.com/un-registered-repo/cyberleek-gateway-finder/master/find_cyberleek_gateways.py
```

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


## 🔧 How It Works

1. **Discovers 300+ gateways** from the AR.IO network peer list
2. **Tests availability** - checks which ones can serve Cyberleek content
3. **Verifies security** - confirms SSL certificates, AR.IO node status, and registry membership
4. **Measures performance** - times response latency for each gateway
5. **Returns safe results** - only shows gateways that pass safety checks, sorted by speed

### Technical Details
- Uses the AR.IO network's `/ar-io/peers` endpoint for gateway discovery
- Performs parallel HTTP requests for fast testing (300+ gateways in ~30 seconds)
- Validates SSL/TLS certificates to prevent MITM attacks
- Checks AR.IO registry membership to filter out untrusted nodes
- Assigns safety scores (0-4) based on multiple criteria
- Zero external dependencies - uses only Python standard library

## 🔍 SEO Keywords

Gta 6 leak, gta 6 leak website, cant find link to gta 6 build, gta 6 pc build, Arweave gateway finder, Cyberleek access, Cyberleek mirror, ArNS resolver, AR.IO gateway list, decentralized web access, permanent storage gateway, Arweave gateway discovery, Arweave mirror finder, ArNS name resolution, Arweave content delivery, gateway timeout fix, Arweave alternative gateway, AR.IO network tools, decentralized gateway finder, Arweave Python tool

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

---

## 🌐 Use Cases

- **Gateway redundancy** - Always have backup access when primary gateway fails
- **Performance optimization** - Find the fastest gateway for your location
- **Censorship resistance** - Access content through decentralized mirror network
- **Network research** - Analyze AR.IO gateway availability and distribution
- **Development testing** - Test Arweave applications across multiple gateways
- **Educational purposes** - Learn about decentralized content delivery networks

## 🔗 Related Projects

- **[Arweave](https://arweave.org)** - Permanent, decentralized data storage protocol
- **[AR.IO](https://ar.io)** - Decentralized gateway network for Arweave
- **[ArNS](https://arns.app)** - Arweave Name System for human-readable addresses

## 💰 Support

If you find this tool useful, Bitcoin donations are appreciated:

**BTC:** `bc1q7wlprmc20rdjyqjsghkhtnmndjs4dpmq26sz6h`

## 📄 License

MIT License - See LICENSE file for details
