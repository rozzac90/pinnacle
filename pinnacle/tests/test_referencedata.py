
import unittest
import unittest.mock as mock

from pinnacle.apiclient import APIClient
from pinnacle.endpoints.referencedata import ReferenceData


class ReferenceDataTest(unittest.TestCase):

    def setUp(self):
        client = APIClient('username', 'password')
        self.reference_data = ReferenceData(client)

    @mock.patch('pinnacle.endpoints.referencedata.ReferenceData.process_response')
    @mock.patch('pinnacle.endpoints.referencedata.ReferenceData.request', return_value=mock.Mock())
    def test_get_sports(self, mock_request, mock_process_response):
        self.reference_data.get_sports()

        mock_request.assert_called_once_with("GET", method='v2/sports', session=None)
        assert mock_process_response.call_count == 1

    @mock.patch('pinnacle.endpoints.referencedata.ReferenceData.process_response')
    @mock.patch('pinnacle.endpoints.referencedata.ReferenceData.request', return_value=mock.Mock())
    def test_get_currencies(self, mock_request, mock_process_response):
        self.reference_data.get_currencies()

        mock_request.assert_called_once_with("GET", method='v2/currencies', session=None)
        assert mock_process_response.call_count == 1

    @mock.patch('pinnacle.endpoints.referencedata.ReferenceData.process_response')
    @mock.patch('pinnacle.endpoints.referencedata.ReferenceData.request', return_value=mock.Mock())
    def test_get_periods(self, mock_request, mock_process_response):
        self.reference_data.get_periods(sport_id=1)

        mock_request.assert_called_once_with("GET", method='v1/periods', params={'sportId': 1}, session=None)
        assert mock_process_response.call_count == 1

    @mock.patch('pinnacle.endpoints.referencedata.ReferenceData.process_response')
    @mock.patch('pinnacle.endpoints.referencedata.ReferenceData.request', return_value=mock.Mock())
    def test_get_leagues(self, mock_request, mock_process_response):
        self.reference_data.get_leagues(sport_id=1)

        mock_request.assert_called_once_with("GET", method='v2/leagues', params={'sportId': 1}, session=None)
        assert mock_process_response.call_count == 1

if __name__=='__main__':
    unittest.main()