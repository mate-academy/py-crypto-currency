# app/test_main.py
from unittest.mock import patch
from app.main import cryptocurrency_action


def test_buy_more_cryptocurrency() -> None:
    """
    Test case: predicted rate is > 5% higher than current rate.
    """
    with patch("app.main.get_exchange_rate_prediction", return_value=110):
        assert cryptocurrency_action(100) == "Buy more cryptocurrency", (
            "Should suggest buying more cryptocurrency when predicted rate "
            "is significantly higher."
        )


def test_sell_all_cryptocurrency() -> None:
    """
    Test case: predicted rate is > 5% lower than current rate.
    """
    with patch("app.main.get_exchange_rate_prediction", return_value=90):
        assert cryptocurrency_action(100) == "Sell all your cryptocurrency", (
            "Should suggest selling cryptocurrency when predicted rate is "
            "significantly lower."
        )


def test_do_nothing() -> None:
    """
    Test case: predicted rate is within 5% of the current rate.
    """
    with patch("app.main.get_exchange_rate_prediction", return_value=102):
        assert cryptocurrency_action(100) == "Do nothing", (
            "Should suggest doing nothing when predicted rate is close to "
            "the current rate."
        )


def test_boundary_5_percent_higher() -> None:
    """
    Test case: predicted rate is exactly 5% higher than the current rate.
    """
    with patch("app.main.get_exchange_rate_prediction", return_value=105):
        assert cryptocurrency_action(100) == "Buy more cryptocurrency", (
            "Should suggest buying when predicted rate is exactly 5% higher."
        )


def test_boundary_5_percent_lower() -> None:
    """
    Test case: predicted rate is exactly 5% lower than the current rate.
    """
    with patch("app.main.get_exchange_rate_prediction", return_value=95):
        assert cryptocurrency_action(100) == "Sell all your cryptocurrency", (
            "Should suggest selling when predicted rate is exactly 5% lower."
        )
