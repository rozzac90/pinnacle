
import unittest
import unittest.mock as mock

from pinnacle.apiclient import APIClient
from pinnacle.endpoints.account import Account


class AccountTest(unittest.TestCase):

    def setUp(self):
        client = APIClient('username', 'password')
        self.account = Account(client)

    @mock.patch('pinnacle.endpoints.account.Account.process_response')
    @mock.patch('pinnacle.endpoints.account.Account.request', return_value=mock.Mock())
    def test_get_account(self, mock_request, mock_process_response):
        self.account.get_account()

        mock_request.assert_called_once_with("GET", method='v1/client/balance', session=None)
        assert mock_process_response.call_count == 1
