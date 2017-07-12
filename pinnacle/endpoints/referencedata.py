import datetime

from pinnacle import resources
from pinnacle.endpoints.baseendpoint import BaseEndpoint


class ReferenceData(BaseEndpoint):

    def get_sports(self, session=None):
        """
        Get all sports.
        
        :param session: requests session to be used.
        :return: list of sports.
        """
        date_time_sent = datetime.datetime.utcnow()
        response = self.request("GET", self.client.url, 'v2/sports', session=session)
        return self.process_response(
            response.json().get('sports', []), resources.SportsDetails, date_time_sent, datetime.datetime.utcnow()
        )

    def get_currencies(self, session=None):
        """
        Get currencies accepted.
        
        :param session: requests session to be used.
        :return: supported currencies.
        """
        date_time_sent = datetime.datetime.utcnow()
        response = self.request("GET", self.client.url, 'v2/currencies', session=session)
        return self.process_response(
            response.json().get('currencies', []), resources.CurrencyDetails, date_time_sent, datetime.datetime.utcnow()
        )
