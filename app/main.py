import random
from typing import Union


def get_exchange_rate_prediction(exchange_rate: Union[int, float]) -> float:
    if random.choice(["increase", "decrease"]) == "increase":
        return round(exchange_rate / random.random(), 2)
    return round(exchange_rate * random.random(), 2)


def cryptocurrency_action(current_rate: Union[int, float]) -> str:
    """
    Determines the action to take based on the predicted exchange rate.

    Args:
        current_rate (float): Current exchange rate of the cryptocurrency.

    Returns:
        str: Suggested action:
             - "Buy more cryptocurrency" if the predicted rate is >= 5% higher.
             - "Sell all your cryptocurrency" if the predicted rate is <= 5% lower.
             - "Do nothing" otherwise.
    """
    prediction_rate = get_exchange_rate_prediction(current_rate)
    if prediction_rate / current_rate >= 1.05:  # >= 5% higher
        return "Buy more cryptocurrency"
    if prediction_rate / current_rate <= 0.95:  # <= 5% lower
        return "Sell all your cryptocurrency"
    return "Do nothing"
