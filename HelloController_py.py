import requests
import json
from pprint import pprint
import urllib.parse


class HelloController():
    """For getting data from the WealthSimple API
    """

    def __init__(self, credentials):
        """Constructor for the class, only parameter is the credentials
        that Ross gave us in the form of a dictionary
        """
        self.credentials = {"object": "application",
                            "id": 66,
                            "name": "Black Swan",
                            "uid": "f8f8763b60e6e2a73d3e5c2b455b95d9eefee96e072dd5c9f1fd63144e166703",
                            "secret": "5bb7db765ea8906ffa308c351e70cc4682bf420262c99fe1030a642ac4c37acb",
                            "confidential": "true",
                            "redirect_uri": [
                                "https://localhost:3000/auth"
                            ],
                            "scopes": [
                                "read",
                                "write"
                            ],
                            "application_family_id": "null",
                            "integration_policy": {
                                "api_version": "v1",
                                "authentication": [
                                    "authorization_code",
                                    "refresh_token"
                                ],
                                "user_roles": [],
                                "userless_endpoints": {},
                                "version": "v1",
                                "abilities": []
                            },
                            "first_party": "false",
                            "created_at": "2018-05-31T23:30:32Z",
                            "updated_at": "2018-05-31T23:30:32Z"
                            }

    def generate_url_with_params(self, url: str, params: dict):
        """This will use urllib to append the parameters to the end of the url
        code from: https://stackoverflow.com/questions/2506379/add-params-to-given-url-in-python

        url - the url of interest
        params - a dictionary of the parameters to be appended
        returns - a string containing the modified url
        """
        url_parts = list(urllib.parse.urlparse(url))
        query = dict(urllib.parse.parse_qsl(url_parts[4]))
        query.update(params)
        url_parts[4] = urllib.parse.urlencode(query)
        url_with_params = urllib.parse.urlunparse(url_parts)
        return url_with_params

    def get_user_auth_url(self):
        """Getting the authorization_code (aka authorization grant) requires
        approving access for another user to take your account information
        which you must do manually in the browser (might be able to automate
        using Selenium to interact with the webpage, but too much work for now)

        returns - a string containing the url to approve access to the account
                  and get the authorization code
        """
        APPLICATION_ID = self.credentials['uid']
        REDIRECT_URI = self.credentials['redirect_uri'][0]
        response_type = 'code'
        scope = self.credentials['scopes'][0]
        state = '1234'

        user_auth_url = "https://staging.wealthsimple.com/oauth/authorize"
        user_auth_params = {'client_id': APPLICATION_ID,
                            'redirect_uri': REDIRECT_URI,
                            'response_type': response_type,
                            'scope': scope,
                            'state': state
                            }

        user_auth_url_params = self.generate_url_with_params(user_auth_url,
                                                             user_auth_params
                                                             )
        # open this address in your browser of choice
        print(user_auth_url_params)
        code = input(
            "After logging into the above URL and authorizing, what's the key after 'code=' and before '&' in the URL? ")
        return code

    def token_exchange(self, _authorization_code: str):
        """Exhange the authorization_code received earlier for an access token from
        the authorization server

        returns - a string containing the access token
        """
        APPLICATION_ID = self.credentials['uid']
        APPLICATION_SECRET = self.credentials['secret']
        REDIRECT_URI = self.credentials['redirect_uri'][0]
        grant_type = self.credentials['integration_policy']['authentication'][0]

        token_exchange_url = "https://api.sandbox.wealthsimple.com/v1/oauth/token"
        token_exchange_params = {'client_id': APPLICATION_ID,
                                 'client_secret': APPLICATION_SECRET,
                                 'grant_type': grant_type,
                                 'redirect_uri': REDIRECT_URI,
                                 'code': _authorization_code
                                 }
        token_exchange_url_params = self.generate_url_with_params(token_exchange_url,
                                                                  token_exchange_params
                                                                  )
        response = requests.post(token_exchange_url_params)
        json_data = json.loads(response.text)
        access_token = json_data['access_token']
        print('access token is: ' + access_token)
        return access_token

    def get_data(self, endpoint: str):
        """Get data from the endpoint specified

		returns - json from API
		"""
        # After you run this once you can comment this out and replace access_token
        # with the actual key to save typing it in every time
        # authorization_code = self.get_user_auth_url()

        # Now swap this authorization code for an access token
        # access_token = self.token_exchange(authorization_code)
        access_token = '963104cc8b49ecdbbff848f5bd1011b7df3eb348fd3c8cbc4f133288845b9347'

        # Use access_token to get information from the server
        # Instead of -H in the URL like the documentation show python appends headers
        # using a dictionary
        headers = {'Authorization': 'Bearer %s' % access_token}
        response = requests.get("https://api.sandbox.wealthsimple.com/v1/%s" % endpoint,
                                headers=headers)
        # pprint(response.text)
        return response.text


# Replace this with your credentials provided by Ross, they're in this format
creds = {
    "application": {
        "name": "Black Swan",
        "redirect_uri": ["https://localhost:3000/auth"],
        "scopes": ["read"],
        "confidential": 'true',
        "application_family_id": 'null',
        "integration_policy": {
            "api_version": "v1",
            "authentication": ["authorization_code", "refresh"],
            "version": "v1"
        }
    }
}
data_getter = HelloController(creds)
# Replace 'users' with whichever endpoint you want to call
data_getter.get_data('accounts')
