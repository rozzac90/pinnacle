
import os
import unittest
import requests
from requests.auth import HTTPBasicAuth

from pinnacle.baseclient import BaseClient
from pinnacle.exceptions import PasswordError

class BaseClientTest(unittest.TestCase):

    def test_baseclient_init(self):
        client = BaseClient(username='username', password='password')
        assert client.username == 'username'
        assert client.password == 'password'
        assert client.url == 'https://api.pinnacle.com/'
        assert isinstance(client.session, requests.Session)
        assert client.headers == {'Content-Type': 'application/json', 'Accept': 'application/json'}
        assert isinstance(client.auth, HTTPBasicAuth)

    def test_get_password(self):
        if 'PINNACLE_PW' in os.environ:
            client = BaseClient(username='username')
            assert client.password == os.environ['PINNACLE_PW']
        else:
            with self.assertRaises(PasswordError):
                BaseClient(username='username')
