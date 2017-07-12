import datetime

from pinnacle import resources
from pinnacle.endpoints.baseendpoint import BaseEndpoint


class Account(BaseEndpoint):

    def get_account(self, session=None):
        """
        Get account info.
        
        :return: account info
        """
        date_time_sent = datetime.datetime.utcnow()
        response = self.request("GET", method='v1/client/balance', session=session)
        return self.process_response(
            response.json(), resources.AccountDetails, date_time_sent, datetime.datetime.utcnow()
        )
