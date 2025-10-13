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
