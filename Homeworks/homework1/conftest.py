import pytest
import requests
import yaml

login_path = 'gateway/login'

@pytest.fixture()
def config() -> dict:
    with open('config.yaml') as f:
        return yaml.safe_load(f)


@pytest.fixture()
def token(config) -> str:
    request = requests.post(url=f"{config['url']}/{login_path}", data={"username": config['login'], "password": config['password']})
    return request.json()['token']

