import unittest
from checkout import invoice_line

class CheckoutTests(unittest.TestCase):
    def test_invoice_contract(self):
        self.assertEqual(invoice_line('20', 2, '0.25'), {'total': '30.00', 'quantity': 2})
