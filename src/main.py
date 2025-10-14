"""Command-line entrypoint for the coingecko-cli project.

This module provides a simple argparse-based CLI with four subcommands:
- ping: check API availability
- price: get the price for one or more coin ids
- trending: list trending coins
- exchanges: list exchanges with pagination options

For now the commands simply print the parsed arguments.
"""
from __future__ import annotations

import argparse
import sys
from src import api


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="coingecko-cli")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # ping
    subparsers.add_parser("ping", help="Ping the CoinGecko API")

    # price
    price_parser = subparsers.add_parser(
        "price", help="Get current price(s) for coin id(s)"
    )
    price_parser.add_argument(
        "coin_ids",
        nargs="+",
        help="One or more CoinGecko coin ids (e.g. bitcoin ethereum)",
    )

    # trending
    subparsers.add_parser("trending", help="Show trending coins")

    # exchanges
    exchanges_parser = subparsers.add_parser(
        "exchanges", help="List exchanges (supports pagination)"
    )
    exchanges_parser.add_argument(
        "--page",
        type=int,
        default=1,
        help="Page number (1-indexed)",
    )
    exchanges_parser.add_argument(
        "--per-page",
        type=int,
        default=100,
        help="Number of items per page",
    )

    return parser


def main(argv: list[str] | None = None) -> int:
    """Parse CLI args and execute the chosen command."""
    argv = argv if argv is not None else sys.argv[1:]
    parser = build_parser()
    args = parser.parse_args(argv)

    # --- Start Replacing Here ---
    try:
        if args.command == "ping":
            data = api.ping_api()
            print("✅ CoinGecko API Status: OK")
            print(data)
        # In your main() function, replace the placeholder "price" block
        elif args.command == "price":
            data = api.get_price(args.coin_ids)
            print("--- Crypto Prices ---")
            # The data is a dictionary, like {'bitcoin': {'usd': 60000, 'usd_market_cap': 12000...}}
            for coin_id, result in data.items():
                price = result.get('usd', 'N/A')
                market_cap = result.get('usd_market_cap', 'N/A')
                # The :_ format adds comma separators to large numbers for readability
                print(f"{coin_id.capitalize()}:")
                print(f"  Price: ${price:,.2f}")
                print(f"  Market Cap: ${market_cap:,.2f}")
            print("---------------------")
        # In your main() function, replace the placeholder "trending" and "exchanges" blocks

        elif args.command == "trending":
            data = api.get_trending_coins()
            print("--- Top Trending Coins ---")
            # The data is a dict {'coins': [{'item': {'name': 'Bitcoin', ...}}]}
            for coin in data.get('coins', []):
                item = coin.get('item', {})
                print(f"- {item.get('name', 'N/A')} ({item.get('symbol', 'N/A').upper()})")
            print("----------------------------")

        elif args.command == "exchanges":
            data = api.get_exchanges(per_page=args.per_page, page=args.page)
            print(f"--- Top {args.per_page} Exchanges (Page {args.page}) ---")
            for exchange in data:
                name = exchange.get('name', 'N/A')
                rank = exchange.get('trust_score_rank', 'N/A')
                print(f"#{rank}: {name}")
            print("---------------------------------")

    except Exception as e:
        print(f"❌ Error: An unexpected error occurred: {e}", file=sys.stderr)
        return 1 # Return a non-zero exit code to indicate failure
    # --- End Replacing Here ---

    return 0 # Return 0 for success


if __name__ == "__main__":
    raise SystemExit(main())
