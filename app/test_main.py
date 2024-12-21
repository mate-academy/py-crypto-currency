from app.main import cryptocurrency_action
from unittest.mock import patch


@patch("app.main.get_exchange_rate_prediction")
def test_sell_all_cryptocurrency(
    mock_get_exchange_rate_prediction: type
) -> None:
    mock_get_exchange_rate_prediction.return_value = 94
    result = cryptocurrency_action(100)
    assert result == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_buy_more_cryptocurrency(
    mock_get_exchange_rate_prediction: type
) -> None:
    mock_get_exchange_rate_prediction.return_value = 106
    result = cryptocurrency_action(100)
    assert result == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_upper_boundary(
    mock_get_exchange_rate_prediction: type
) -> None:
    mock_get_exchange_rate_prediction.return_value = 105
    result = cryptocurrency_action(100)
    assert result == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_lower_boundary(
    mock_get_exchange_rate_prediction: type
) -> None:
    mock_get_exchange_rate_prediction.return_value = 95
    result = cryptocurrency_action(100)
    assert result == "Do nothing"
