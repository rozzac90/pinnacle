# -*- coding: utf-8 -*-
import uuid
import datetime

from pinnacle import resources
from pinnacle.enums import OddsFormat, Boolean, WinRiskType, FillType
from pinnacle.endpoints.baseendpoint import BaseEndpoint
from pinnacle.utils import clean_locals


class Betting(BaseEndpoint):

    def get_bets(self, betids=None, betlist=None, unique_request_ids=None, from_date=None, to_date=None,
                 bet_statuses=None, sort_dir=None, page_size=None, from_record=None, session=None):
        """
        Get running bets or bets settled within the last 30 days.
        
        :param from_date: start date for bet query. Maximum 30 days between from_date and to_date. 
                          Required when betlist parameter is supplied.
        :param to_date: end date for bet query. to_date value is exclusive, meaning it cannot be equal to from_date.
                        Required when betlist parameter is supplied.
        :param betlist: type of bets to filter for, see pinnacle.enums.BetListType.
        :param betids: list of bet IDs, max 100, works for non settled bets and bets settled in the last 30 days.
        :param unique_request_ids: list of uniqueRequestIds to query bets placed within the last 30 mins and straight bets only. 
                                   If specified, is treated with highest priority, all other parameters are ignored. Maximum is 10 ids.
        :param bet_statuses: Type of bet statuse to filter for, see pinnacle.enums.BetStatusesType. 
                             This works only in conjustion with betlist, as additional filter. 
        :param sort_dir: Type of bet statuse to filter for, see pinnacle.enum.SortDirType. 
                         This works only in conjustion with betlist, as additional filter.
        :param page_size: Page size in case. Max is 1000. Respected only when querying by date range.
        :param from_record: Starting record (inclusive) of the result. Respected only when querying by date range. 
                            To fetch next page set it to toRecord+1
        :param session: requests session to be used.
        :returns: All bets fitting the filtered arguments supplied. 
        """
        from_date = from_date.strftime('%Y-%m-%d') if from_date is not None else from_date
        to_date = to_date.strftime('%Y-%m-%d') if to_date is not None else to_date
        params = clean_locals(locals())
        date_time_sent = datetime.datetime.utcnow()
        response = self.request("GET", method='v3/bets', params=params, session=session)
        return self.process_response(
            response.json(), resources.BetDetails, date_time_sent, datetime.datetime.utcnow()
        )

    def place_bet(self, sport_id, event_id, line_id, period_number, bet_type, stake, team=None, side=None,
                  alt_line_id=None, win_risk_stake=WinRiskType.Risk.value, accept_better_line=Boolean.TRUE.name,
                  odds_format=OddsFormat.Decimal.value, fill_type=FillType.Normal, pitcher1_must_start=None,
                  pitcher2_must_start=None, customer_reference=None, session=None):
        """
        Place bet in the system.
        
        :param sport_id: sport identification
        :param event_id: event identification
        :param line_id: Line identification
        :param period_number: This represents the period of the match. 
        :param bet_type: type of bet to be placed, see pinnacle.enums.BetType
        :param stake: Wagered amount in Clients currency
        :param team: Chosen team type. This is needed only for SPREAD, MONEYLINE and TEAM_TOTAL_POINTS bet types
        :param side: Chosen side. This is needed only for TOTAL_POINTS and TEAM_TOTAL_POINTS bet type
        :param alt_line_id: Alternate line identification
        :param win_risk_stake: Whether the stake amount is risk or win amount
        :param accept_better_line: Whether or not to accept a bet when there is a line change in favor of the client.
        :param odds_format: Bet is processed with this odds format.
        :param fill_type: FillAndKill, if stake > maxbet will fill max bet. FillMaxLimit, ignore stake and stake to max bet.
        :param pitcher1_must_start: Baseball only. Refers to the pitcher for TEAM_TYPE. Team1. 
                                    Only for MONEYLINE bet type, for all other bet types this has to be TRUE.
        :param pitcher2_must_start: Baseball only. Refers to the pitcher for TEAM_TYPE. Team2. 
                                    Only for MONEYLINE bet type, for all other bet types this has to be TRUE.
        :param customer_reference: Reference for customer to use.
        :param session: requests session to be used.
        :return: bet success/failure.
        """
        unique_request_id = str(uuid.uuid4())
        params = clean_locals(locals())
        date_time_sent = datetime.datetime.utcnow()
        response = self.request("POST", method='/v2/bets/straight', data=params, session=session)
        return self.process_response(
            response.json(), resources.PlaceBetDetails, date_time_sent, datetime.datetime.utcnow()
        )

    def place_special_bet(self, line_id, special_id, contestant_id, stake, win_risk_stake=WinRiskType.Risk.value,
                          odds_format=OddsFormat.Decimal.value, accept_better_line=Boolean.TRUE.name, session=None):
        """
        Place special bet in the system.
        
        :param line_id: Line identification
        :param special_id: Special identification.
        :param contestant_id: Contestant identification.
        :param stake: Wagered amount in Clients currency.
        :param win_risk_stake: Whether the stake amount is risk or win amount
        :param odds_format: Bet is processed with this odds format.
        :param accept_better_line: Whether or not to accept a bet when there is a line change in favor of the client.
        :param session: requests session to be used.
        :return: bet success/failure.
        """
        unique_request_id = str(uuid.uuid4())
        params = {'bets': [clean_locals(locals())]}
        date_time_sent = datetime.datetime.utcnow()
        response = self.request("POST", method='v1/bets/special', data=params, session=session)
        return self.process_response(
            response.json().get('bets', []), resources.PlaceSpecialBetDetails, date_time_sent, datetime.datetime.utcnow()
        )

    def place_teaser_bet(self):
        raise NotImplementedError

    def place_parlay_bet(self):
        raise NotImplementedError
