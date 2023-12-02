from unittest import TestCase
from unittest.mock import patch
from app.main import cryptocurrency_action

class TestCryptocurrencyAction(TestCase):
    @patch('app.main.get_exchange_rate_prediction')
    def test_buy_more_cryptocurrency(self, mock_get_exchange_rate_prediction):
        mock_get_exchange_rate_prediction.return_value = 1.05
        result = cryptocurrency_action(1)
        self.assertEqual(result, "Buy more cryptocurrency")

    @patch('app.main.get_exchange_rate_prediction')
    def test_sell_all_cryptocurrency(self, mock_get_exchange_rate_prediction):
        mock_get_exchange_rate_prediction.return_value = 0.95
        result = cryptocurrency_action(1)
        self.assertEqual(result, "Sell all your cryptocurrency")

    @patch('app.main.get_exchange_rate_prediction')
    def test_do_nothing(self, mock_get_exchange_rate_prediction):
        mock_get_exchange_rate_prediction.return_value = 1
        result = cryptocurrency_action(1)
        self.assertEqual(result, "Do nothing")
