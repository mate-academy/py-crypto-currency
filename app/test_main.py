import pytest
from unittest import mock
from app.main import cryptocurrency_action


@pytest.fixture
def mocked_exchange_rate_prediction() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") \
            as mocked_prediction:
        yield mocked_prediction


def test_buy_more_cryptocurrency(
        mocked_exchange_rate_prediction: int) -> None:
    mocked_exchange_rate_prediction.return_value = 1.06
    assert cryptocurrency_action(1) == "Buy more cryptocurrency"


def test_sell_cryptocurrency_cryptocurrency(
        mocked_exchange_rate_prediction: int) -> None:
    mocked_exchange_rate_prediction.return_value = 0.94
    assert cryptocurrency_action(1) == "Sell all your cryptocurrency"


def test_utmost_case_one(
        mocked_exchange_rate_prediction: int) -> None:
    mocked_exchange_rate_prediction.return_value = 1.05
    assert cryptocurrency_action(1) == "Do nothing"


def test_utmost_case_two(mocked_exchange_rate_prediction: int) -> None:
    mocked_exchange_rate_prediction.return_value = 0.95
    assert cryptocurrency_action(1) == "Do nothing"
