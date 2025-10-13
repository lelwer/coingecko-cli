"""Small CoinGecko API helpers used by the CLI.

This module provides a single function `ping_api` which hits the
CoinGecko `/ping` endpoint and returns the parsed JSON response.
"""
from typing import Any, Dict

import requests


COINGECKO_BASE = "https://api.coingecko.com/api/v3"


def ping_api(timeout: float = 5.0) -> Dict[str, Any]:
    """Ping the CoinGecko API /ping endpoint.

    Makes a GET request to the CoinGecko `/ping` endpoint and returns
    the parsed JSON on success.

    Args:
        timeout: number of seconds to wait for the HTTP response.

    Returns:
        The JSON-decoded response as a dictionary.

    Raises:
        requests.exceptions.RequestException: for network-related errors.
        RuntimeError: for non-success HTTP responses or invalid JSON.
    """
    url = f"{COINGECKO_BASE}/ping"
    try:
        resp = requests.get(url, timeout=timeout)
    except requests.exceptions.RequestException as exc:
        # Network-level errors (DNS, connection, timeouts, etc.)
        raise

    if not resp.ok:
        # Non-2xx responses
        raise RuntimeError(f"CoinGecko /ping returned status {resp.status_code}")

    try:
        data = resp.json()
    except ValueError as exc:
        # Invalid JSON
        raise RuntimeError("CoinGecko /ping returned invalid JSON") from exc

    return data


def get_price(coin_ids: list[str], timeout: float = 5.0) -> Dict[str, Any]:
    """Fetch current price (and market cap) for one or more coins.

    Calls the CoinGecko `/simple/price` endpoint and returns the parsed JSON
    response. The `ids` query parameter must be a comma-separated string of
    coin ids. This helper requests prices in USD and includes the market cap
    (usd_market_cap) in the response.

    Args:
        coin_ids: A list of CoinGecko coin id strings (for example,
            ['bitcoin', 'ethereum']). Must contain at least one id.
        timeout: Number of seconds to wait for the HTTP response.

    Returns:
        The JSON-decoded response as a dictionary mapping coin ids to price
        objects.

    Raises:
        ValueError: If `coin_ids` is empty.
        requests.exceptions.RequestException: For network-related errors.
        RuntimeError: For non-success HTTP responses or invalid JSON.
    """
    if not coin_ids:
        raise ValueError("coin_ids must contain at least one coin id")

    ids_param = ",".join(coin_ids)
    url = f"{COINGECKO_BASE}/simple/price"
    params = {
        "ids": ids_param,
        "vs_currencies": "usd",
        "include_market_cap": "true",
    }

    try:
        resp = requests.get(url, params=params, timeout=timeout)
    except requests.exceptions.RequestException:
        # Propagate network-level exceptions to the caller
        raise

    if not resp.ok:
        raise RuntimeError(
            f"CoinGecko /simple/price returned status {resp.status_code}"
        )

    try:
        data = resp.json()
    except ValueError as exc:
        raise RuntimeError("CoinGecko /simple/price returned invalid JSON") from exc

    return data


def get_trending_coins(timeout: float = 5.0) -> Dict[str, Any]:
    """Retrieve trending coins from CoinGecko.

    Calls the CoinGecko `/search/trending` endpoint and returns the parsed
    JSON response. The result typically contains a `coins` key with a list of
    trending coin objects.

    Args:
        timeout: Number of seconds to wait for the HTTP response.

    Returns:
        The JSON-decoded response as a dictionary.

    Raises:
        requests.exceptions.RequestException: For network-related errors.
        RuntimeError: For non-success HTTP responses or invalid JSON.
    """
    url = f"{COINGECKO_BASE}/search/trending"
    try:
        resp = requests.get(url, timeout=timeout)
    except requests.exceptions.RequestException:
        # Propagate network-level exceptions to the caller
        raise

    if not resp.ok:
        raise RuntimeError(
            f"CoinGecko /search/trending returned status {resp.status_code}"
        )

    try:
        data = resp.json()
    except ValueError as exc:
        raise RuntimeError("CoinGecko /search/trending returned invalid JSON") from exc

    return data


def get_exchanges(per_page: int = 100, page: int = 1, timeout: float = 5.0) -> list[dict[str, any]]:
    """List exchanges from CoinGecko.

    Calls the CoinGecko `/exchanges` endpoint and returns the parsed JSON
    response. The endpoint supports pagination via `per_page` and `page`.

    Args:
        per_page: Number of exchanges to return per page (max depends on API).
        page: Page number to retrieve (1-indexed).
        timeout: Number of seconds to wait for the HTTP response.

    Returns:
        The JSON-decoded response as a dictionary or list containing exchange
        objects, depending on the API response.

    Raises:
        ValueError: If `per_page` or `page` are not positive.
        requests.exceptions.RequestException: For network-related errors.
        RuntimeError: For non-success HTTP responses or invalid JSON.
    """
    if per_page <= 0:
        raise ValueError("per_page must be a positive integer")
    if page <= 0:
        raise ValueError("page must be a positive integer")

    url = f"{COINGECKO_BASE}/exchanges"
    params = {"per_page": str(per_page), "page": str(page)}

    try:
        resp = requests.get(url, params=params, timeout=timeout)
    except requests.exceptions.RequestException:
        raise

    if not resp.ok:
        raise RuntimeError(f"CoinGecko /exchanges returned status {resp.status_code}")

    try:
        data = resp.json()
    except ValueError as exc:
        raise RuntimeError("CoinGecko /exchanges returned invalid JSON") from exc

    return data
