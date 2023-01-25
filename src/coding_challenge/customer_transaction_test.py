import unittest
from unittest import mock

from .customer_transaction import TransactionSolution


def mocked_requests_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    if args[0] == "https://cdn.sablecard.com/challenge/transactions-v2.json":
        return MockResponse([{"amount": 1000}], 200)

    return MockResponse(None, 404)


class TransactionSolutionTestCase(unittest.TestCase):

    # Now we must patch 'my.great.package.requests.get'
    @mock.patch("requests.get", side_effect=mocked_requests_get)
    def test_fetch(self, mock_get):
        s = TransactionSolution()
        self.assertEqual(s.totalAmount(), 1000)
