import json


class BaseEndpoint(object):

    def __init__(self, parent):
        """
        :param parent: API client.
        """
        self.client = parent

    def request(self, request_method, method, params={}, data={}, session=None):
        """
        :param request_method: type of request to be sent.
        :param method: Matchbook method to be used.
        :param params: Params to be used in request.
        :param data: data to be sent in request body.
        :param session: Requests session to be used, reduces latency.
        """
        session = session or self.client.session
        request_url = '%s%s' % (self.client.url, method)
        response = session.request(
            request_method, request_url, params=params, data=json.dumps(data),
            auth=self.client.auth, headers=self.client.headers,
        )
        return response

    @staticmethod
    def process_response(response_json, resource, date_time_sent, date_time_received=None):
        """
        :param response_json: Response in json format
        :param resource: Resource data structure
        :param date_time_sent: Date time sent
        :param date_time_received: Date time received response from request
        """
        if isinstance(response_json, list):
            return [
                resource(date_time_sent=date_time_sent, TIMESTAMP=date_time_received.strftime('%Y-%m-%d %H:%M:%S.%f'),
                         **x).json() for x in response_json]
        else:
            response_result = response_json.get('result', response_json)
            if isinstance(response_result, list):
                return [resource(date_time_sent=date_time_sent,
                                 TIMESTAMP=date_time_received.strftime('%Y-%m-%d %H:%M:%S.%f'),
                                 **x).json() for x in response_result]
            else:
                return resource(date_time_sent=date_time_sent,
                                TIMESTAMP=date_time_received.strftime('%Y-%m-%d %H:%M:%S.%f'),
                                **response_result).json()
