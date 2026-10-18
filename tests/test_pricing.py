import unittest
from decimal import Decimal
from pricing import discounted_total


class PricingTests(unittest.TestCase):
    def test_small_order_rounds_once(self):
        self.assertEqual(discounted_total('0.05', 3, '0.10'), Decimal('0.14'))

    def test_regular_order(self):
        self.assertEqual(discounted_total('20', 2, '0.25'), Decimal('30.00'))

    def test_negative_quantity_rejected(self):
        with self.assertRaises(ValueError):
            discounted_total('20', -1, '0.25')

    def test_invalid_discount_rejected(self):
        with self.assertRaises(ValueError):
            discounted_total('20', 2, '1.25')

    def test_no_discount(self):
        self.assertEqual(discounted_total('1.29', 3, '0'), Decimal('3.87'))
