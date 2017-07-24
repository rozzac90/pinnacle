
import unittest
import unittest.mock as mock

from pinnacle.apiclient import APIClient
from pinnacle.endpoints.marketdata import MarketData


class MarketDataTest(unittest.TestCase):

    def setUp(self):
        client = APIClient('username', 'password')
        self.market_data = MarketData(client)

    @mock.patch('pinnacle.endpoints.marketdata.MarketData.process_response')
    @mock.patch('pinnacle.endpoints.marketdata.MarketData.request', return_value=mock.Mock())
    def test_get_sports(self, mock_request, mock_process_response):
        self.market_data.get_fixtures(sport_id=1, league_ids=[1, 2], since=10000)

        mock_request.assert_called_once_with(
            "GET", method='v1/fixtures', params={'sportId': 1, 'leagueIds': [1, 2], 'since': 10000}, session=None
        )
        assert mock_process_response.call_count == 1

    @mock.patch('pinnacle.endpoints.marketdata.MarketData.process_response')
    @mock.patch('pinnacle.endpoints.marketdata.MarketData.request', return_value=mock.Mock())
    def test_get_settled_fixtures(self, mock_request, mock_process_response):
        self.market_data.get_settled_fixtures(sport_id=1, league_ids=[1, 2], since=10000)

        mock_request.assert_called_once_with(
            "GET", method='v1/fixtures/settled', params={'sportId': 1, 'leagueIds': [1, 2], 'since': 10000}, session=None
        )
        assert mock_process_response.call_count == 1

    @mock.patch('pinnacle.endpoints.marketdata.MarketData.process_response')
    @mock.patch('pinnacle.endpoints.marketdata.MarketData.request', return_value=mock.Mock())
    def test_get_special_fixtures(self, mock_request, mock_process_response):
        self.market_data.get_special_fixtures(sport_id=1, league_ids=[1, 2], special_id=10, since=10000)

        mock_request.assert_called_once_with("GET", method='v1/fixtures/special',
                                             params={'sportId': 1, 'leagueIds': [1, 2], 'specialId': 10, 'since': 10000},
                                             session=None)
        assert mock_process_response.call_count == 1

    @mock.patch('pinnacle.endpoints.marketdata.MarketData.process_response')
    @mock.patch('pinnacle.endpoints.marketdata.MarketData.request', return_value=mock.Mock())
    def test_get_settled_special_fixtures(self, mock_request, mock_process_response):
        self.market_data.get_settled_special_fixtures(sport_id=1, league_ids=[1, 2], since=10000)

        mock_request.assert_called_once_with("GET", method='v1/fixtures/special/settled',
                                             params={'sportId': 1, 'leagueIds': [1, 2], 'since': 10000}, session=None)
        assert mock_process_response.call_count == 1

    @mock.patch('pinnacle.endpoints.marketdata.MarketData.process_response')
    @mock.patch('pinnacle.endpoints.marketdata.MarketData.request', return_value=mock.Mock())
    def test_get_inrunning(self, mock_request, mock_process_response):
        self.market_data.get_inrunning()

        mock_request.assert_called_once_with("GET", method='v1/inrunning', params={}, session=None)
        assert mock_process_response.call_count == 1

    @mock.patch('pinnacle.endpoints.marketdata.MarketData.process_response')
    @mock.patch('pinnacle.endpoints.marketdata.MarketData.request', return_value=mock.Mock())
    def test_get_odds(self, mock_request, mock_process_response):
        self.market_data.get_odds(sport_id=1, league_ids=[1, 2], since=10000)

        mock_request.assert_called_once_with(
            "GET", method='v1/odds',
            params={'sportId': 1, 'leagueIds': [1, 2], 'oddsFormat': 'DECIMAL', 'since': 10000}, session=None
        )
        assert mock_process_response.call_count == 1

    @mock.patch('pinnacle.endpoints.marketdata.MarketData.process_response')
    @mock.patch('pinnacle.endpoints.marketdata.MarketData.request', return_value=mock.Mock())
    def test_get_special_odds(self, mock_request, mock_process_response):
        self.market_data.get_special_odds(sport_id=1, league_ids=[1, 2], special_id=1000, since=10000)

        mock_request.assert_called_once_with(
            "GET", method='v1/odds/special',
            params={'sportId': 1, 'leagueIds': [1, 2], 'oddsFormat': 'DECIMAL', 'specialId': 1000, 'since': 10000},
            session=None
        )
        assert mock_process_response.call_count == 1

    @mock.patch('pinnacle.endpoints.marketdata.MarketData.process_response')
    @mock.patch('pinnacle.endpoints.marketdata.MarketData.request', return_value=mock.Mock())
    def test_get_line(self, mock_request, mock_process_response):
        self.market_data.get_line(sport_id=1, league_id=2, event_id=100, period_number=0, bet_type='MONEYLINE')

        mock_request.assert_called_once_with(
            "GET", method='v1/line',
            params={'sportId': 1, 'leagueId': 2, 'eventId': 100, 'periodNumber': 0,
                    'betType': 'MONEYLINE', 'oddsFormat': 'DECIMAL'},
            session=None
        )
        assert mock_process_response.call_count == 1

    @mock.patch('pinnacle.endpoints.marketdata.MarketData.process_response')
    @mock.patch('pinnacle.endpoints.marketdata.MarketData.request', return_value=mock.Mock())
    def test_get_special_lines(self, mock_request, mock_process_response):
        self.market_data.get_special_lines(special_id=102131, contestant_id=1000)

        mock_request.assert_called_once_with(
            "GET", method='v1/line/special',
            params={'specialId': 102131, 'contestantId': 1000, 'oddsFormat': 'DECIMAL'},
            session=None
        )
        assert mock_process_response.call_count == 1

    def test_get_teaser_groups(self):
        with self.assertRaises(NotImplementedError):
            self.market_data.get_teaser_groups()

    def test_get_teaser_odds(self):
        with self.assertRaises(NotImplementedError):
            self.market_data.get_teaser_odds()

    def test_get_teaser_lines(self):
        with self.assertRaises(NotImplementedError):
            self.market_data.get_teaser_lines()

    def test_get_parlay_lines(self):
        with self.assertRaises(NotImplementedError):
            self.market_data.get_parlay_lines()
