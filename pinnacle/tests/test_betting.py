
import unittest
import unittest.mock as mock

from pinnacle.apiclient import APIClient
from pinnacle.endpoints.betting import Betting
from pinnacle.enums import WinRiskType, Boolean, OddsFormat


class BettingTest(unittest.TestCase):

    def setUp(self):
        client = APIClient('username', 'password')
        self.betting = Betting(client)

    @mock.patch('pinnacle.endpoints.betting.Betting.process_response')
    @mock.patch('pinnacle.endpoints.betting.Betting.request', return_value=mock.Mock())
    def test_get_bets(self, mock_request, mock_process_response):
        self.betting.get_bets(betids=[1, 2, 3, 4])

        mock_request.assert_called_once_with("GET", method='v3/bets', params={'betids': [1, 2, 3, 4]}, session=None)
        assert mock_process_response.call_count == 1

    @mock.patch('pinnacle.endpoints.betting.Betting.process_response')
    @mock.patch('pinnacle.endpoints.betting.Betting.request', return_value=mock.Mock())
    def test_place_bet(self, mock_request, mock_process_response):
        self.betting.place_bet(
            sport_id=1, event_id=2, line_id=10001, period_number=1, bet_type='MONEYLINE', stake=10.5, team=None,
            side=None, alt_line_id=None, win_risk_stake=WinRiskType.Risk.value, accept_better_line=Boolean.TRUE.value,
            odds_format=OddsFormat.Decimal.value, pitcher1_must_start=None,
            pitcher2_must_start=None, customer_reference=None, session=None
        )
        req_method, params = mock_request.call_args

        assert req_method[0] == "POST"
        assert params['method'] == '/v2/bets/straight'
        assert params['data']['sportId'] == 1
        assert params['data']['eventId'] == 2
        assert params['data']['lineId'] == 10001
        assert params['data']['periodNumber'] == 1
        assert params['data']['betType'] == 'MONEYLINE'
        assert params['data']['stake'] == 10.5
        assert params['data']['winRiskStake'] == 'RISK'
        assert params['data']['acceptBetterLine'] == 1
        assert params['data']['oddsFormat'] == 'DECIMAL'

        assert mock_process_response.call_count == 1

    @mock.patch('pinnacle.endpoints.betting.Betting.process_response')
    @mock.patch('pinnacle.endpoints.betting.Betting.request', return_value=mock.Mock())
    def test_place_special_bet(self, mock_request, mock_process_response):
        self.betting.place_special_bet(
            line_id=10001, special_id=20002, contestant_id=1, stake=12, win_risk_stake=WinRiskType.Win.value,
            odds_format=OddsFormat.American.value, accept_better_line=Boolean.TRUE.value, session=None
        )
        req_method, params = mock_request.call_args

        assert req_method[0] == "POST"
        assert params['method'] == 'v1/bets/special'
        assert isinstance(params['data']['bets'], list)
        assert params['data']['bets'][0]['specialId'] == 20002
        assert params['data']['bets'][0]['lineId'] == 10001
        assert params['data']['bets'][0]['contestantId'] == 1
        assert params['data']['bets'][0]['stake'] == 12
        assert params['data']['bets'][0]['winRiskStake'] == 'WIN'
        assert params['data']['bets'][0]['acceptBetterLine'] == 1
        assert params['data']['bets'][0]['oddsFormat'] == 'AMERICAN'

        assert mock_process_response.call_count == 1

    def test_place_teaser_bet(self):
        with self.assertRaises(NotImplementedError):
            self.betting.place_teaser_bet()

    def test_place_parlay_bet(self):
        with self.assertRaises(NotImplementedError):
            self.betting.place_parlay_bet()
