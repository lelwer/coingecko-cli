# coingecko-cli

![Python pytest](https://github.com/your-username/coingecko-cli/actions/workflows/tests.yml/badge.svg)
![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

A small, well-tested command-line interface (CLI) for fetching cryptocurrency data from the public CoinGecko API. This tool provides a simple set of commands to check API availability, retrieve current prices, show trending coins, and list top exchanges.

## Features

* ✅ **Ping API**: Check whether the CoinGecko API is reachable.
* 💰 **Get Prices**: Fetch the current USD price and market cap for one or more coins (e.g., `bitcoin ethereum`).
* 🔥 **View Trending**: List the top-7 trending coins on CoinGecko.
* 🏦 **List Exchanges**: List top exchanges with support for pagination.

## Installation

**1. Clone the repository:**
```bash
git clone [https://github.com/your-username/coingecko-cli.git](https://github.com/your-username/coingecko-cli.git)
cd coingecko-cli
2. Create and activate a virtual environment:

Windows (PowerShell):

PowerShell

python -m venv venv
.\venv\Scripts\Activate.ps1
Mac/Linux (Bash):

Bash

python3 -m venv venv
source venv/bin/activate
3. Install dependencies:

Bash

pip install -r requirements.txt
Usage
All commands are run from the root of the project directory.

Ping the API
Bash

python -m src.main ping
<details>
<summary>Example Output</summary>

✅ CoinGecko API Status: OK
{'gecko_says': '(V3) To the Moon!'}
</details>

Get the price and market cap for one or more coins
Bash

python -m src.main price bitcoin solana
<details>
<summary>Example Output</summary>

--- Crypto Prices ---
Bitcoin:
  Price: $67,123.00
  Market Cap: $1,322,456,789,123.00
Solana:
  Price: $145.67
  Market Cap: $65,987,654,321.00
---------------------
</details>

Show top-7 trending coins
Bash

python -m src.main trending
List exchanges (with pagination)
Bash

python -m src.main exchanges --per-page 5 --page 2
API
This project is powered by the free and public CoinGecko API.

Development
This project uses pytest for testing. All network calls are mocked using unittest.mock to ensure tests are fast and deterministic. A GitHub Actions workflow automatically runs the test suite on all pushes and pull requests to the main branch.

License
This project is licensed under the MIT License. See the LICENSE file for details.

