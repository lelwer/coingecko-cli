# Project Name: coingecko-cli (CoinGecko Command-Line Interface)

## Overview
A command-line tool to fetch cryptocurrency data from the public CoinGecko API. Users can check API status, get coin prices, view trending coins, and list top exchanges. This project is for practicing what is possible and emphasizes professional practices like testing, CI/CD, and documentation, all developed with AI assistance.

## API Integration
- **API:** CoinGecko Public API V3
- **Base URL:** https://docs.coingecko.com/
- **Authentication:** None required.
- **Key Endpoints:**
  - `/ping` - Check API server status.
  - `/simple/price` - Get current price of any crypto.
  - `/search/trending` - Get top trending coins.
  - `/exchanges` - Get top exchanges by trust score rank.
- **Data Format:** JSON

## CLI Commands
- `cg ping` - Checks if the CoinGecko API is responsive.
- `cg price <coin_id...>` - Fetches the current price and market cap for one or more cryptocurrencies.
- `cg trending` - Displays the top trending coins on CoinGecko.
- `cg exchanges` - Lists the top cryptocurrency exchanges by trust score rank.

## Technical Stack
- Python 3.10+
- `argparse` for CLI argument parsing
- `requests` library for API calls
- `pytest` for testing with mocking (`unittest.mock`)
- GitHub Actions for CI/CD

## Code Organization
- `src/main.py` - Entry point and argparse setup.
- `src/api.py` - Handles all interaction with the CoinGecko API.
- `tests/` - Test files with mocked API responses.

## Standards
- Follow PEP 8 style guidelines.
- All functions and classes must have docstrings.
- All API calls must be mocked in tests; no real network requests during testing.
- Graceful error handling with `try/except` blocks for API calls and data parsing.