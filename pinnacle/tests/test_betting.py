
import unittest
import unittest.mock as mock

from pinnacle.apiclient import APIClient
from pinnacle.endpoints.betting import Betting


class BettingTest(unittest.TestCase):

    def setUp(self):
        client = APIClient('username', 'password')
        self.betting = Betting(client)

    @mock.patch('pinnacle.endpoints.betting.Betting.process_response')
    @mock.patch('pinnacle.endpoints.betting.Betting.request', return_value=mock.Mock())
    def test_get_bets(self, mock_request, mock_process_response):
        self.betting.get_bets(betids=[1, 2, 3, 4])

        mock_request.assert_called_once_with("GET", method='v1/bets', params={'betIds': [1, 2, 3, 4]}, session=None)
        assert mock_process_response.call_count == 1
