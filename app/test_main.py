from unittest.mock import patch
from unittest.mock import Mock

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "prediction_rate,current_rate,result",
    [
        pytest.param(
            150,
            100,
            "Buy more cryptocurrency",
            id="should buy more cryptocurrency, if fraction > 1.05"
        ),
        pytest.param(
            40,
            50,
            "Sell all your cryptocurrency",
            id="should sell all cryptocurrency, if fraction < 0.95"
        ),
        pytest.param(
            205,
            200,
            "Do nothing",
            id="should do nothing, if 0.95 < fraction < 1.05"
        ),
        pytest.param(
            47.5,
            50,
            "Do nothing",
            id="should do nothing, if fraction = 0.95"
        ),
        pytest.param(
            105,
            100,
            "Do nothing",
            id="should do nothing, if fraction = 1.05"
        )
    ]
)
@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_prediction(
        mock_get_exchange: Mock,
        current_rate: int | float,
        prediction_rate: int | float,
        result: str
) -> None:
    mock_get_exchange.return_value = prediction_rate
    assert cryptocurrency_action(current_rate) == result
