from app.main import cryptocurrency_action

from unittest import mock

import pytest


@pytest.mark.parametrize(
    "current_rate, predicted_rate, expected",
    [
        (100, 106, "Buy more cryptocurrency"),
        (100, 94, "Sell all your cryptocurrency"),
        (100, 100, "Do nothing"),
        (100, 105, "Do nothing"),
        (100, 95, "Do nothing"),
    ],
)
def test_cryptocurrency_action(
    current_rate: int | float,
    predicted_rate: int | float,
    expected: str
) -> None:
    with mock.patch(
        "app.main.get_exchange_rate_prediction", return_value=predicted_rate
    ):
        assert cryptocurrency_action(current_rate) == expected
