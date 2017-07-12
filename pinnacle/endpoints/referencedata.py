import datetime

from pinnacle import resources
from pinnacle.endpoints.baseendpoint import BaseEndpoint
from pinnacle.utils import clean_locals


class ReferenceData(BaseEndpoint):

    def get_sports(self, session=None):
        """
        Get all sports.
        
        :param session: requests session to be used.
        :return: list of sports.
        """
        date_time_sent = datetime.datetime.utcnow()
        response = self.request("GET", method='v2/sports', session=session)
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
        response = self.request("GET", method='v2/currencies', session=session)
        return self.process_response(
            response.json().get('currencies', []), resources.CurrencyDetails, date_time_sent, datetime.datetime.utcnow()
        )

    def get_periods(self, sport_id, session=None):
        """
        Get periods for a given sport.
        
        :param sport_id: id of the sport to get periods breakdown for.
        :param session: requests session to be used.
        :return: sport periods breakdown.
        """
        params = clean_locals(locals())
        date_time_sent = datetime.datetime.utcnow()
        response = self.request("GET", method='v1/periods', params=params, session=session)
        return self.process_response(
            response.json().get('periods', []), resources.PeriodDetails, date_time_sent, datetime.datetime.utcnow()
        )

    def get_leagues(self, sport_id, session=None):
        """
        Get leagues contained for a given sport.

        :param sport_id: id of the sport to get periods breakdown for.
        :param session: requests session to be used.
        :return: leagues for a given sport.
        """
        params = clean_locals(locals())
        date_time_sent = datetime.datetime.utcnow()
        response = self.request("GET", method='v2/leagues', params=params, session=session)
        return self.process_response(
            response.json().get('leagues', []), resources.LeagueDetails, date_time_sent, datetime.datetime.utcnow()
        )
