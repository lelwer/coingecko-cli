# coingecko-cli

![CI](https://github.com/lelwer/coingecko-cli/actions/workflows/tests.yml/badge.svg)
![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

A small, well-tested command-line interface (CLI) for fetching cryptocurrency data from the public CoinGecko API. This tool provides a simple set of commands to check API availability, retrieve current prices, show trending coins, and list top exchanges.

## Features

- ✅ Ping API: Check whether the CoinGecko API is reachable.
- 💰 Get Prices: Fetch the current USD price and market cap for one or more coins (e.g., `bitcoin ethereum`).
- 🔥 View Trending: List the top-7 trending coins on CoinGecko.
- 🏦 List Exchanges: List top exchanges with support for pagination.

## Installation

Requirements
- Python 3.10+

1. Clone the repository

```bash
git clone https://github.com/your-username/coingecko-cli.git
cd coingecko-cli
```

2. Create and activate a virtual environment

Windows (PowerShell):

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

macOS / Linux (bash):

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

## Usage

All commands are run from the project root. The CLI entrypoint is `src/main.py`.

- Ping the API

```powershell
python -m src.main ping
```

Example output:

```text
✅ CoinGecko API Status: OK
{'gecko_says': '(V3) To the Moon!'}
```

- Get the price and market cap for one or more coins

```powershell
python -m src.main price bitcoin
python -m src.main price bitcoin ethereum
```

Example output:

```text
--- Crypto Prices ---
Bitcoin:
  Price: $67,123.00
  Market Cap: $1,322,456,789,123.00
Solana:
  Price: $145.67
  Market Cap: $65,987,654,321.00
---------------------
```

- Show top-7 trending coins

```powershell
python -m src.main trending
```

Example output:

```text
--- Top-7 Trending Coins ---
- Bitcoin (BTC)
- Solana (SOL)
----------------------------
```

- List exchanges (with pagination)

```powershell
python -m src.main exchanges --per-page 5 --page 2
```

Example output:

```text
--- Top 5 Exchanges (Page 2) ---
#1: Binance
#2: Kraken
---------------------------------
```

## API

This project is powered by the free and public CoinGecko API: https://api.coingecko.com/api/v3

## Development

- Tests: `pytest` (network calls are mocked using `unittest.mock`).
- CI: GitHub Actions runs the test suite on pushes and pull requests to `main`.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

