import pytest
from unittest import mock
from typing import Union

from .main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate,pred_rate,expected_result",
    [
        (1, 1.06, "Buy more cryptocurrency"),
        (1, 0.94, "Sell all your cryptocurrency"),
        (1, 0.9, "Sell all your cryptocurrency"),
        (10, 3, "Sell all your cryptocurrency"),
        (1, 0.95, "Do nothing"),
        (1, 1.05, "Do nothing"),
        (44, 43, "Do nothing"),
    ]
)
def test_get_exchange_rate_prediction(
        current_rate: Union[int, float],
        pred_rate: Union[int, float],
        expected_result: str
) -> None:
    rate_pred = "app.main.get_exchange_rate_prediction"
    with mock.patch(rate_pred, return_value=pred_rate) as mocked_rate_pred:
        assert cryptocurrency_action(current_rate) == expected_result
        mocked_rate_pred.assert_called_once_with(current_rate)
