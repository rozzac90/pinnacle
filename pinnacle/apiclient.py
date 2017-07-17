from pinnacle.baseclient import BaseClient
from pinnacle import endpoints


class APIClient(BaseClient):

    def __init__(self, username, password=None):
        super(APIClient, self).__init__(username, password)

        self.betting = endpoints.Betting(self)
        self.account = endpoints.Account(self)
        self.market_data = endpoints.MarketData(self)
        self.reference_data = endpoints.ReferenceData(self)

    def __repr__(self):
        return '<APIClient [%s]>' % self.username

    def __str__(self):
        return 'APIClient'