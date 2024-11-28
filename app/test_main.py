from typing import Union
import pytest
from unittest import mock
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, predicted_rate, expected_result",
    [
        (1.0, 1.06, "Buy more cryptocurrency"),
        (1.0, 0.95, "Do nothing"),
        (1.0, 0.94, "Sell all your cryptocurrency"),
        (1.06, 1.86, "Do nothing"),
        (1.0, 1.05, "Do nothing")
    ]
)
def test_cryptocurrency_action(
        current_rate: Union[int, float],
        predicted_rate: Union[int, float],
        expected_result: str
) -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as mock_get:
        mock_get.return_value = predicted_rate
        result = cryptocurrency_action(current_rate)
        assert result == expected_result
