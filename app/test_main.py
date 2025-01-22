import unittest
from unittest.mock import patch
from app.main import cryptocurrency_action


class TestCryptocurrencyAction(unittest.TestCase):
    @patch("app.main.get_exchange_rate_prediction")
    def test_exchange_rate_is_more_than_5_percent_higher(
            self,
            mock_exchange: int | float
    ) -> None:
        mock_exchange.return_value = 1.06
        current_rate = 1
        self.assertEqual(
            cryptocurrency_action(current_rate), "Buy more cryptocurrency"
        )

    @patch("app.main.get_exchange_rate_prediction")
    def test_exchange_rate_is_more_than_5_percent_lower(
            self,
            mock_exchange: int | float
    ) -> None:
        mock_exchange.return_value = 0.94
        current_rate = 1
        self.assertEqual(
            cryptocurrency_action(current_rate), "Sell all your cryptocurrency"
        )

    @patch("app.main.get_exchange_rate_prediction")
    def test_different_is_not_much(self, mock_exchange: int | float) -> None:
        mock_exchange.return_value = 1.04
        current_rate = 1
        self.assertEqual(
            cryptocurrency_action(current_rate), "Do nothing"
        )
        mock_exchange.return_value = 0.96
        self.assertEqual(
            cryptocurrency_action(current_rate), "Do nothing"
        )


    @patch("app.main.get_exchange_rate_prediction")
    def test_prediction_rate_equals_0_95(self, mock_exchange) -> None:
        mock_exchange.return_value = 0.95
        current_rate = 1
        self.assertEqual(cryptocurrency_action(current_rate), "Do nothing")


    @patch("app.main.get_exchange_rate_prediction")
    def test_prediction_rate_equals_1_05(self, mock_exchange) -> None:
        mock_exchange.return_value = 1.05
        current_rate = 1
        self.assertEqual(cryptocurrency_action(current_rate), "Do nothing")


if __name__ == "__main__":
    unittest.main()
