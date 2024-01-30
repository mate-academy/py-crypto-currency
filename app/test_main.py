import unittest
from unittest.mock import patch
from app.main import cryptocurrency_action


class TestCryptocurrencyAction(unittest.TestCase):

    @patch("app.main.get_exchange_rate_prediction")
    def test_buy_more_cryptocurrency(
            self,
            mock_get_exchange_rate_prediction: patch
    ) -> None:
        mock_get_exchange_rate_prediction.return_value = 1.06
        result = cryptocurrency_action(1.0)
        self.assertEqual(result, "Buy more cryptocurrency")

    @patch("app.main.get_exchange_rate_prediction")
    def test_sell_all_cryptocurrency(
            self,
            mock_get_exchange_rate_prediction: patch
    ) -> None:
        mock_get_exchange_rate_prediction.return_value = 0.94
        result = cryptocurrency_action(1.0)
        self.assertEqual(result, "Sell all your cryptocurrency")

    @patch("app.main.get_exchange_rate_prediction")
    def test_do_nothing(
            self,
            mock_get_exchange_rate_prediction: patch
    ) -> None:
        mock_get_exchange_rate_prediction.return_value = 1.02
        result = cryptocurrency_action(1.0)
        self.assertEqual(result, "Do nothing")

    @patch("app.main.get_exchange_rate_prediction")
    def test_rate_105_percent_do_nothing(
            self,
            mock_get_exchange_rate_prediction: patch
    ) -> None:
        mock_get_exchange_rate_prediction.return_value = 1.05
        result = cryptocurrency_action(1.0)
        self.assertEqual(result, "Do nothing")

    @patch("app.main.get_exchange_rate_prediction")
    def test_rate_95_percent_do_nothing(
            self,
            mock_get_exchange_rate_prediction: patch
    ) -> None:
        mock_get_exchange_rate_prediction.return_value = 0.95
        result = cryptocurrency_action(1.0)
        self.assertEqual(result, "Do nothing")
