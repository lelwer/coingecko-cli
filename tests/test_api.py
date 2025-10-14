from unittest.mock import patch, Mock

from src.api import ping_api, get_price, get_trending_coins, get_exchanges, COINGECKO_BASE


def test_ping_api_success():
    expected = {"gecko_says": "test successful"}
    url = f"{COINGECKO_BASE}/ping"

    mock_resp = Mock()
    mock_resp.ok = True
    mock_resp.json.return_value = expected

    with patch("src.api.requests.get", return_value=mock_resp) as mock_get:
        result = ping_api()

    # requests.get was called once with the ping URL and default timeout
    mock_get.assert_called_once()
    called_args, called_kwargs = mock_get.call_args
    assert called_args[0] == url
    assert called_kwargs['timeout'] == 5.0  # <-- Correct placement

    # Ensure the function returned the mocked JSON
    assert result == expected


def test_get_price_success():
    # Fake JSON payload for bitcoin and ethereum
    expected = {
        "bitcoin": {"usd": 60000, "usd_market_cap": 1200000000},
        "ethereum": {"usd": 3000, "usd_market_cap": 350000000},
    }

    url = f"{COINGECKO_BASE}/simple/price"

    mock_resp = Mock()
    mock_resp.ok = True
    mock_resp.json.return_value = expected

    # Patch requests.get and call get_price with two coin ids
    with patch("src.api.requests.get", return_value=mock_resp) as mock_get:
        result = get_price(["bitcoin", "ethereum"])

    # requests.get should have been called once with the URL and params
    mock_get.assert_called_once()
    called_args, called_kwargs = mock_get.call_args
    assert called_args[0] == url

    # Verify params dict
    expected_params = {
        "ids": "bitcoin,ethereum",
        "vs_currencies": "usd",
        "include_market_cap": "true",
    }
    assert called_kwargs["params"] == expected_params
    assert called_kwargs["timeout"] == 5.0

    # Ensure the function returned the mocked JSON
    assert result == expected


def test_get_trending_coins_success():
    expected = {"coins": [{"item": {"id": "bitcoin"}}]}
    url = f"{COINGECKO_BASE}/search/trending"

    mock_resp = Mock()
    mock_resp.ok = True
    mock_resp.json.return_value = expected

    with patch("src.api.requests.get", return_value=mock_resp) as mock_get:
        # import and call the function from src.api to match import style
        result = get_trending_coins()

    mock_get.assert_called_once()
    called_args, called_kwargs = mock_get.call_args
    assert called_args[0] == url
    assert called_kwargs["timeout"] == 5.0

    assert result == expected


def test_get_exchanges_success():
    # Fake response is a list of exchanges
    expected = [{"id": "binance"}, {"id": "kraken"}]
    url = f"{COINGECKO_BASE}/exchanges"

    mock_resp = Mock()
    mock_resp.ok = True
    mock_resp.json.return_value = expected

    with patch("src.api.requests.get", return_value=mock_resp) as mock_get:
        # call get_exchanges with specific pagination
        result = get_exchanges(per_page=50, page=2)

    mock_get.assert_called_once()
    called_args, called_kwargs = mock_get.call_args
    assert called_args[0] == url

    # params should include per_page and page as strings
    expected_params = {"per_page": "50", "page": "2"}
    assert called_kwargs["params"] == expected_params
    assert called_kwargs["timeout"] == 5.0

    assert result == expected


def test_ping_api_failure_network_error():
    import requests
    import pytest

    # Configure the patched requests.get to raise a RequestException
    with patch("src.api.requests.get", side_effect=requests.exceptions.RequestException("network down")) as mock_get:
        with pytest.raises(requests.exceptions.RequestException):
            ping_api()

    # Ensure requests.get was attempted
    mock_get.assert_called_once()