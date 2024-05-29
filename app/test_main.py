import pytest
from unittest import mock

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, prediction_rate, advice",
    [
        (100, 106, "Buy more cryptocurrency"),
        (100, 94, "Sell all your cryptocurrency"),
        (100, 105, "Do nothing"),
        (100, 95, "Do nothing")
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        rate_mocked_f: mock.Mock,
        current_rate: int | float,
        prediction_rate: int | float,
        advice: str
) -> None:
    rate_mocked_f.return_value = prediction_rate
    assert cryptocurrency_action(current_rate) == advice
