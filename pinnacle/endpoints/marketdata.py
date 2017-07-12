import datetime

from pinnacle import resources
from pinnacle.endpoints.baseendpoint import BaseEndpoint
from pinnacle.utils import clean_locals


class MarketData(BaseEndpoint):

    def get_fixtures(self):
        raise NotImplementedError

    def get_special_fixtures(self):
        raise NotImplementedError

    def get_inrunning(self):
        raise NotImplementedError

    def get_odds(self):
        raise NotImplementedError

    def get_special_odds(self):
        raise NotImplementedError

    def get_line(self):
        raise NotImplementedError

    def get_special_lines(self):
        raise NotImplementedError
