import requests


def __request(type: str, url: str, token: str, params=None) -> requests.Response:
    if params is None:
        params = {}

    if type == "get":
        return requests.get(url=url, headers={"X-Auth-Token": token}, params=params)
    elif type == "post":
        return requests.post(url=url, headers={"X-Auth-Token": token}, params=params)


def get(url: str, token: str, params=None) -> requests.Response:
    return __request(type='get', url=url, token=token, params=params)


def post(url: str, token: str, params=None) -> requests.Response:
    return __request(type='post', url=url, token=token, params=params)

