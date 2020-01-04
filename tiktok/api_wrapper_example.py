class ApiExample:
    """ Wrapper interface to interact with Example API.
    """

    def __init__(self, domain: str="example.com", protocol: str="http"):
        self.base_url = f"{protocol}://{domain}/"

    def get_profile(self, oauth_token: str, access_token: str) -> dict:
        """ Retrieve profile given identification details.

        Args:
            oauth_token: (string). The oauth_token for the account.
            access_token: (string). The access_token for the account.

        Return:
            (dict). profile data as a dictionary. 
        """
        endpoint = "get_profile"
        url = self.base + endpoint
        response = http.get(url, params={"oauth": oauth_token})
        return response

    def get_latest_posts(self, oauth_token: str, access_token: str, max_n int=20) -> list:
        """ Retrieve the `max_n` latest posts published by owner of oauth_token.

        Args:
            oauth_token: (string). The oauth_token for the account.
            access_token: (string). The access_token for the account.

        Return:
            (list). List of `max_n` latest posts represented as dictionaries.
        """
        endpoint = "posts"
        url = self.base + endpoint
        response = http.get(url, params={"oauth": oauth_token})
        return response