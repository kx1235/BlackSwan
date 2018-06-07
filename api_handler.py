"""
Wealthsimple API Handler
Communicates with Wealthsimple API using OAuth 2.0

Created by Bill Ang Li
Jun. 7th, 2018
"""

import requests
import urllib.parse as urlparse
from urllib.parse import urlencode
import json


class Controller:
    """Read and write data using the Wealthsimple API
    """
    credentials: dict

    def __init__(self, credentials: dict):
        """Constructor to create the controller
        """
        self.credentials = credentials

    def generate_url(self, url: str, params: dict) -> str:
        """Generate url using the given parameters

        Code from https://stackoverflow.com/questions/2506379/add-params-to-given-url-in-python
        """
        url_parts = list(urlparse.urlparse(url))
        query = dict(urlparse.parse_qsl(url_parts[4]))
        query.update(params)

        url_parts[4] = urlencode(query)
        url_with_params = urlparse.urlunparse(url_parts)
        return url_with_params

    def request_access(self) -> str:
        """Obtain consent from user to use the Wealthsimple API"""
        url = 'https://staging.wealthsimple.com/oauth/authorize'
        params = {'client_id': self.credentials['client_id'],
                  'redirect_uri': self.credentials['redirect_uri'],
                  'response_type': self.credentials['response_type'],
                  'scope': self.credentials['scope']
                  }

        url_with_params = self.generate_url(url, params)

        # Provide url to user
        print(url_with_params)
        code = input('What is the code after logging into the above url?')
        self.credentials['code'] = code
        return code

    def token_exchange(self) -> str:
        """Exchange authorization code for access token"""
        url = 'https://api.sandbox.wealthsimple.com/v1/oauth/token'
        params = {'client_id': self.credentials['client_id'],
                  'client_secret': self.credentials['client_secret'],
                  'grant_type': self.credentials['grant_type'],
                  'redirect_uri': self.credentials['redirect_uri'],
                  'code': self.credentials['code'],
                  }

        response = requests.post(url, data=params)
        json_data = json.loads(response.text)
        access_token = json_data['access_token']
        print("Access token: " + access_token)
        self.credentials['access_token'] = access_token
        return access_token

    def get_data(self, endpoint: str) -> None:
        """Get data from the Wealthsimple account
        """
        if 'code' not in self.credentials or 'access_token' not in self.credentials:
            # Obtain access token if it has not done yet
            self.request_access()
            self.token_exchange()

        url = 'https://api.sandbox.wealthsimple.com/v1/%s' % endpoint
        headers = {'Authorization': 'Bearer %s' % self.credentials['access_token']}
        response = requests.get(url, headers=headers)
        json_data = json.loads(response.text)
        print(json.dumps(json_data, indent=4, sort_keys=True))


credentials = {'client_id': 'f8f8763b60e6e2a73d3e5c2b455b95d9eefee96e072dd5c9f1fd63144e166703',
               'redirect_uri': 'https://localhost:3000/auth',
               'response_type': 'code',
               'state': 'random',
               'scope': 'read write',
               'client_secret': '5bb7db765ea8906ffa308c351e70cc4682bf420262c99fe1030a642ac4c37acb',
               'grant_type': 'authorization_code'}

if __name__ == "__main__":
    controller = Controller(credentials)
    endpoint = input("Enter endpoint")
    controller.get_data(endpoint)
