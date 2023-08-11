from typing import Union
from unittest import mock
from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_that_the_function_should_return_bay(
        mocked_prediction: Union[int, float]
) -> None:
    mocked_prediction.return_value = 10.6
    assert cryptocurrency_action(10) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_that_the_function_should_return_sell(
        mocked_prediction: Union[int, float]
) -> None:
    mocked_prediction.return_value = 9.4
    assert cryptocurrency_action(10) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_of_what_the_function_should_return_at_105(
        mocked_prediction: Union[int, float]
) -> None:
    mocked_prediction.return_value = 10.5
    assert cryptocurrency_action(10) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_of_what_the_function_should_return_at_95(
        mocked_prediction: Union[int, float]
) -> None:
    mocked_prediction.return_value = 9.5
    assert cryptocurrency_action(10) == "Do nothing"
