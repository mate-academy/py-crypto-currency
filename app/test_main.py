from unittest.mock import patch
from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
def test_buy_more_cryptocurrency(mock_get_exchange_rate_prediction: patch) -> None:
    """
    Test case: predicted rate is more than 5% higher than the current rate.
    Expected: "Buy more cryptocurrency".
    """
    mock_get_exchange_rate_prediction.return_value = 110
    assert cryptocurrency_action(100) == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_sell_all_cryptocurrency(mock_get_exchange_rate_prediction: patch) -> None:
    """
    Test case: predicted rate is more than 5% lower than the current rate.
    Expected: "Sell all your cryptocurrency".
    """
    mock_get_exchange_rate_prediction.return_value = 90
    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing(mock_get_exchange_rate_prediction: patch) -> None:
    """
    Test case: predicted rate is within 5% of the current rate.
    Expected: "Do nothing".
    """
    mock_get_exchange_rate_prediction.return_value = 102
    assert cryptocurrency_action(100) == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_boundary_5_percent_higher(mock_get_exchange_rate_prediction: patch) -> None:
    """
    Test case: predicted rate is exactly 5% higher than the current rate.
    Expected: "Do nothing".
    """
    mock_get_exchange_rate_prediction.return_value = 105
    assert cryptocurrency_action(100) == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_boundary_5_percent_lower(mock_get_exchange_rate_prediction: patch) -> None:
    """
    Test case: predicted rate is exactly 5% lower than the current rate.
    Expected: "Do nothing".
    """
    mock_get_exchange_rate_prediction.return_value = 95  # Exactly 5% lower
    assert cryptocurrency_action(100) == "Do nothing"
