import unittest

from pinnacle.apiclient import APIClient
from pinnacle.endpoints import Betting, Account, MarketData, ReferenceData


class APIClientTest(unittest.TestCase):

    def test_apiclient_init(self):
        client = APIClient('username', 'password')
        assert str(client) == 'APIClient'
        assert repr(client) == '<APIClient [username]>'
        assert isinstance(client.betting, Betting)
        assert isinstance(client.account, Account)
        assert isinstance(client.market_data, MarketData)
        assert isinstance(client.reference_data, ReferenceData)
