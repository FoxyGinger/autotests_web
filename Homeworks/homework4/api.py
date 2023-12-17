import logging

import requests


def __request(type: str, url: str, token: str, params=None):
    if params is None:
        params = {}

    logging.debug(f'Отправка запроса {type} "{url}"; token={token}, params={params}')
    try:
        if type == "get":
            response = requests.get(url=url, headers={"X-Auth-Token": token}, params=params)
        elif type == "post":
            response = requests.post(url=url, headers={"X-Auth-Token": token}, params=params)
        else:
            logging.error(f'Unsupported request method: {type}')
            return None

        if response.status_code != 200:
            return None

        return response
    except:
        logging.exception(f'Exception while send request {type.upper()} "{url}"')


def get(url: str, token: str, params=None) -> requests.Response:
    return __request(type='get', url=url, token=token, params=params)


def post(url: str, token: str, params=None) -> requests.Response:
    return __request(type='post', url=url, token=token, params=params)

