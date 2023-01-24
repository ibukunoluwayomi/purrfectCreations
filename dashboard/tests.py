from unittest.mock import patch
from dashboard.views import get_dashboard_data
import unittest
from freezegun import freeze_time


class TestDashboard(unittest.TestCase):
    @patch('pyairtable.Table.all')
    @freeze_time("2021-09-15")
    def test_get_dashboard_data(self, table_all):
        table_all.return_value = []
        assert (0, 0, 0, 0, []) == get_dashboard_data()
        all_orders = [
            {
                "fields": {'order_id': 1, 'order_placed': '2021-09-15', 'product_name': '',
                           'price': 1.0,
                           'first_name': '', 'last_name': '', 'address': '',
                           'email': '', 'order_status': 'shipped'}},
            {
                "fields": {'order_id': 2, 'order_placed': '2021-08-15', 'product_name': '',
                           'price': 2.0,
                           'first_name': '', 'last_name': '', 'address': '',
                           'email': '', 'order_status': 'shipped'},
            },
            {
                "fields": {'order_id': 3, 'order_placed': '2021-07-15', 'product_name': '',
                           'price': 3.0,
                           'first_name': '', 'last_name': '', 'address': '',
                           'email': '', 'order_status': 'shipped'},
            },
            {
                "fields": {'order_id': 4, 'order_placed': '2021-06-15', 'product_name': '',
                           'price': 80.1,
                           'first_name': '', 'last_name': '', 'address': '',
                           'email': '', 'order_status': 'in_progress'},
            }
        ]
        table_all.return_value = all_orders
        expected_total_orders = 4
        expected_total_orders_this_month = 1
        expected_number_of_orders_in_progress = 1
        expected_revenue = 86.1
        expected_recent_orders = [
            {'order_id': 1, 'order_placed': '2021-09-15', 'product_name': '',
             'price': 1.0,
             'first_name': '', 'last_name': '', 'address': '',
             'email': '', 'order_status': 'shipped'},
            {
                'order_id': 2, 'order_placed': '2021-08-15', 'product_name': '',
                'price': 2.0,
                'first_name': '', 'last_name': '', 'address': '',
                'email': '', 'order_status': 'shipped'
            },
            {
                'order_id': 3, 'order_placed': '2021-07-15', 'product_name': '',
                'price': 3.0,
                'first_name': '', 'last_name': '', 'address': '',
                'email': '', 'order_status': 'shipped'
            },
            {
                'order_id': 4, 'order_placed': '2021-06-15', 'product_name': '',
                'price': 80.1,
                'first_name': '', 'last_name': '', 'address': '',
                'email': '', 'order_status': 'in_progress'
            }
        ]
        self.assertEqual(
            (expected_total_orders, expected_total_orders_this_month, expected_number_of_orders_in_progress,
             expected_revenue, expected_recent_orders), get_dashboard_data())


if __name__ == '__main__':
    unittest.main()
