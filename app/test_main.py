from unittest import mock
from pytest import mark

from app.main import cryptocurrency_action


@mark.parametrize(
    "current_rate, predicted_rate, expected_result",
    [
        (1.0, 1.05, "Do nothing"),
        (1.0, 0.95, "Do nothing"),
        (0.95, 1.0, "Buy more cryptocurrency"),
        (1.0, 0.94, "Sell all your cryptocurrency"),
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
    mocked_predicted_rate: mock.Mock,
    current_rate: int | float,
    predicted_rate: int | float,
    expected_result: str
) -> None:
    mocked_predicted_rate.return_value = predicted_rate
    assert cryptocurrency_action(current_rate) == expected_result
