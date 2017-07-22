import datetime

from pinnacle import resources
from pinnacle.enums import OddsFormat
from pinnacle.endpoints.baseendpoint import BaseEndpoint
from pinnacle.utils import clean_locals


class MarketData(BaseEndpoint):

    def get_fixtures(self, sport_id, league_ids=None, since=None, is_live=None, event_ids=None, session=None):
        """
        Get all unsettled fixtures for a given sport.
        
        :param sport_id: id of the sport.
        :param league_ids: list of league ids for given sport.
        :param since: Used to receive incremental updates. Use the value of last from previous fixtures response
        :param is_live: To retrieve ONLY live events set the value to islive =1. 
        :param event_ids: list of event ids to filter for.
        :param session: requests session to be used.
        :return: all non-settled events.
        """
        params = clean_locals(locals())
        date_time_sent = datetime.datetime.utcnow()
        response = self.request("GET", method='v1/fixtures', params=params, session=session)
        return self.process_response(
            response.json(), resources.FixtureDetails, date_time_sent, datetime.datetime.utcnow()
        )

    def get_settled_fixtures(self, sport_id, league_ids=None, since=None, session=None):
        """
        Get fixtures settled within the last 24 hours.
        
        :param sport_id: id of the sport.
        :param league_ids: list of league ids for given sport.
        :param since: Used to receive incremental updates. Use the value of last from previous fixtures response
        :param session: requests session to be used.
        :return: settled fixtures.
        """
        params = clean_locals(locals())
        date_time_sent = datetime.datetime.utcnow()
        response = self.request("GET", method='v1/fixtures/settled', params=params, session=session)
        return self.process_response(
            response.json(), resources.SettledFixtureDetails, date_time_sent, datetime.datetime.utcnow()
        )

    def get_special_fixtures(self, sport_id, league_ids=None, category=None, event_id=None,
                             special_id=None, since=None, session=None):
        """
        Get unsettled special fixtures for given sport.
        
        :param sport_id: id of the sport.
        :param league_ids: list of league ids for given sport.
        :param category: category of the special.
        :param event_id: id of the linked event.
        :param special_id: id of specific special to get.
        :param since: Used to receive incremental updates. Use the value of last from previous fixtures response
        :param session: requests session to be used.
        :return: all non-settled specials (contests)
        """
        params = clean_locals(locals())
        date_time_sent = datetime.datetime.utcnow()
        response = self.request("GET", method='v1/fixtures/settled', params=params, session=session)
        return self.process_response(
            response.json(), resources.SpecialFixtureDetails, date_time_sent, datetime.datetime.utcnow()
        )

    def get_settled_special_fixtures(self, sport_id, league_ids=None, since=None, session=None):
        """
        Get special fixtures settled within the last 24 hours.

        :param sport_id: id of the sport.
        :param league_ids: list of league ids for given sport.
        :param since: Used to receive incremental updates. Use the value of last from previous fixtures response
        :param session: requests session to be used.
        :return: settled special fixtures.
        """
        params = clean_locals(locals())
        date_time_sent = datetime.datetime.utcnow()
        response = self.request("GET", method='v1/fixtures/special/settled', params=params, session=session)
        return self.process_response(
            response.json(), resources.SettledSpecialFixtureDetails, date_time_sent, datetime.datetime.utcnow()
        )

    def get_inrunning(self, session=None):
        """
        Get all events that have a live status associated with them. 
        
        :param session: requests session to be used.
        :return: live events.
        """
        params = clean_locals(locals())
        date_time_sent = datetime.datetime.utcnow()
        response = self.request("GET", method='v1/inrunning', params=params, session=session)
        return self.process_response(
            response.json(), resources.InRunningDetails, date_time_sent, datetime.datetime.utcnow()
        )

    def get_odds(self, sport_id, league_ids=None, event_ids=None, since=None, is_live=None,
                 odds_format=OddsFormat.Decimal.value, session=None):
        """
        Get straight and parlay odds for all non-settled events.
        
        :param sport_id: id of the sport.
        :param league_ids: list of league ids for given sport.
        :param since: Used to receive incremental updates. Use the value of last from previous fixtures response
        :param is_live: To retrieve ONLY live events set the value to islive =1. 
        :param event_ids: list of event ids to filter for.
        :param odds_format: Format in which we return the odds. 
        :param session: requests session to be used. 
        :return: straight and parlay odds for all non-settled events.
        """
        params = clean_locals(locals())
        date_time_sent = datetime.datetime.utcnow()
        response = self.request("GET", method='v1/odds', params=params, session=session)
        return self.process_response(
            response.json(), resources.OddsDetails, date_time_sent, datetime.datetime.utcnow()
        )

    def get_special_odds(self, sport_id, league_ids=None, special_id=None, since=None,
                         odds_format=OddsFormat.Decimal.value, session=None):
        """
        Get special odds for all non-settled events.
        
        :param sport_id: id of the sport.
        :param league_ids: list of league ids for given sport.
        :param special_id: id of specific special to filter for.
        :param odds_format: Format in which we return the odds. 
        :param since: Used to receive incremental updates. Use the value of last from previous fixtures response
        :param session: requests session to be used. 
        :return: special odds for all non-settled events.
        """
        params = clean_locals(locals())
        date_time_sent = datetime.datetime.utcnow()
        response = self.request("GET", method='v1/odds/special', params=params, session=session)
        return self.process_response(
            response.json(), resources.OddsDetails, date_time_sent, datetime.datetime.utcnow()
        )

    def get_line(self, sport_id, league_id, event_id, period_number, bet_type, team=None, side=None, handicap=None,
                 odds_format=OddsFormat.Decimal.value, session=None):
        """
        Get latest odds for a line.
        
        :param sport_id: id of the sport to which the line belongs.
        :param league_id: id of the league to which the line belongs.
        :param event_id: id of the event to which the line belongs.
        :param period_number: This represents the period of the match. 
        :param bet_type: bet_type of the line, see pinnacle.enums.BetType
        :param team: Chosen team type. This is needed only for SPREAD, MONEYLINE and TEAM_TOTAL_POINTS bet types
        :param side: Chosen side. This is needed only for TOTAL_POINTS and TEAM_TOTAL_POINTS bet type
        :param handicap: This is needed for SPREAD, TOTAL_POINTS and TEAM_TOTAL_POINTS bet type
        :param odds_format: Format in which we return the odds. 
        :param session: requests session to be used. 
        :return: latest line.
        """
        params = clean_locals(locals())
        date_time_sent = datetime.datetime.utcnow()
        response = self.request("GET", method='v1/line', params=params, session=session)
        return self.process_response(
            response.json(), resources.LineDetails, date_time_sent, datetime.datetime.utcnow()
        )

    def get_special_lines(self, special_id, contestant_id, odds_format=OddsFormat.Decimal.value, session=None):
        """
        Get latest special line.
        
        :param special_id: id of the special.
        :param contestant_id: id of the participant in the special.
        :param odds_format: Format in which we return the odds.
        :param session: requests session to be used. 
        :return: latest special line.
        """
        params = clean_locals(locals())
        date_time_sent = datetime.datetime.utcnow()
        response = self.request("GET", method='v1/line/special', params=params, session=session)
        return self.process_response(
            response.json(), resources.SpecialLineDetails, date_time_sent, datetime.datetime.utcnow()
        )

    def get_teaser_groups(self):
        raise NotImplementedError

    def get_teaser_odds(self):
        raise NotImplementedError

    def get_teaser_lines(self):
        raise NotImplementedError

    def get_parlay_lines(self):
        raise NotImplementedError
