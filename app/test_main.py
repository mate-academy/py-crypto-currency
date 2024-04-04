from unittest.mock import patch
import pytest
from app.main import cryptocurrency_action


@pytest.mark.parametrize("current_rate, predicted_rate, expected_action", [
    (100, 105, "Do nothing"),
    (100, 95, "Do nothing"),
    (100, 106, "Buy more cryptocurrency"),
    (100, 94, "Sell all your cryptocurrency"),
    (100, 100, "Do nothing"),
])
def test_cryptocurrency_action(
        current_rate: int,
        predicted_rate: int,
        expected_action: str) -> None:
    with patch("app.main.get_exchange_rate_prediction",
               return_value=predicted_rate):
        action = cryptocurrency_action(current_rate)
        assert action == expected_action, (
            f"Expected action '{expected_action}' "
            f"was not returned when prediction_rate "
            f"/ current_rate == {predicted_rate / current_rate}")
