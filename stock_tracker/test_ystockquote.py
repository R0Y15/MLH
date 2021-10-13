import unittest

import ystockquote


class YStockQuoteTestCase(unittest.TestCase):

    def get_everything(self):
        symbol = 'GOOG'
        all_info = ystockquote.get_all(symbol)
        self.assertIsInstance(all_info, dict)
        pc = all_info['previous_close']
        self.assertNotEqual(pc, 'N/A')
        self.assertGreater(float(pc), 0)

    def history_prices(self):
        symbol = 'GOOG'
        start_date = '2013-01-02'
        end_date = '2013-01-15'
        prices = ystockquote.get_historical_prices(
            symbol, start_date, end_date)
        self.assertIsInstance(prices, dict)
        self.assertEqual(len(prices), 10)
        self.assertEqual(sorted(prices.keys())[0], '2013-01-02')
        self.assertEqual(sorted(prices.keys())[-1], end_date)
        self.assertGreater(float(prices[start_date]['Open']), 0.0)
        self.assertGreater(float(prices[start_date]['High']), 0.0)
        self.assertGreater(float(prices[start_date]['Low']), 0.0)
        self.assertGreater(float(prices[start_date]['Close']), 0.0)
        self.assertGreater(float(prices[start_date]['Volume']), 0.0)
        self.assertGreater(float(prices[start_date]['Adj Close']), 0.0)
        self.assertGreater(float(prices[end_date]['Open']), 0.0)
        self.assertGreater(float(prices[end_date]['High']), 0.0)
        self.assertGreater(float(prices[end_date]['Low']), 0.0)
        self.assertGreater(float(prices[end_date]['Close']), 0.0)
        self.assertGreater(float(prices[end_date]['Volume']), 0.0)
        self.assertGreater(float(prices[end_date]['Adj Close']), 0.0)


if __name__ == '__main__':
    unittest.main()
