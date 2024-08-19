from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "predicted_rate: float, current_rate: float, expected_action: str",
    [
        (100.0, 106.0, "Buy more cryptocurrency"),
        (100.0, 94.0, "Sell all your cryptocurrency"),
        (100.0, 104.0, "Do nothing"),
        (100.0, 95.0, "Do nothing"),
        (100.0, 105.0, "Do nothing")
    ]
)
def test_cryptocurrency_action(
        predict_rate: float,
        current_rate: float,
        expected_value: str
) -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as mock_rate:
        mock_rate.return_value = predict_rate

        assert cryptocurrency_action(current_rate) == expected_value
