from unittest import mock
from app.main import cryptocurrency_action


def test_cryptocurrency_action_buy() -> None:
    current_rate: float = 100.0
    # Mock get_exchange_rate_prediction return 6% up
    with mock.patch("app.main.get_exchange_rate_prediction",
                    return_value=106.0):
        result: str = cryptocurrency_action(current_rate)
        assert result == "Buy more cryptocurrency"


def test_cryptocurrency_action_sell() -> None:
    current_rate: float = 100.0
    # Mock get_exchange_rate_prediction return 6% low
    with mock.patch("app.main.get_exchange_rate_prediction",
                    return_value=94.0):
        result: str = cryptocurrency_action(current_rate)
        assert result == "Sell all your cryptocurrency"


def test_cryptocurrency_action_do_nothing_upper_bound() -> None:
    current_rate: float = 100.0
    # Mock get_exchange_rate_prediction return 5% up
    with mock.patch("app.main.get_exchange_rate_prediction",
                    return_value=105.0):
        result: str = cryptocurrency_action(current_rate)
        assert result == "Do nothing"


def test_cryptocurrency_action_do_nothing_lower_bound() -> None:
    current_rate: float = 100.0
    # Mock get_exchange_rate_prediction return 5% low
    with mock.patch("app.main.get_exchange_rate_prediction",
                    return_value=95.0):
        result: str = cryptocurrency_action(current_rate)
        assert result == "Do nothing"
