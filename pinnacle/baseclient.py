
import os
import requests
from requests.auth import HTTPBasicAuth

from pinnacle.exceptions import PasswordError


class BaseClient(object):
    def __init__(self, username, password=None):
        """
        :param username: Pinnacle username.
        :param password: Password for supplied username, if None will look in for PINNACLE_PW in env variables.
        """
        self.username = username
        self.password = password
        self.url = 'https://api.pinnacle.com/'
        self.session = requests.Session()
        self.get_password()

    def get_password(self):
        """If password is not provided will look in environment
        variables for username+'password'
        """
        if self.password is None:
            if os.environ.get('PINNACLE_PW'):
                self.password = os.environ.get('PINNACLE_PW')
            else:
                raise PasswordError()

    @property
    def headers(self):
        """Set headers to be used in API requests."""
        return {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
        }

    @property
    def auth(self):
        """Set auth param to be used in API requests."""
        return HTTPBasicAuth(username=self.username, password=self.password)
