import pytest
import yaml

from module import Site


@pytest.fixture()
def config() -> dict:
    with open('config.yaml') as f:
        return yaml.safe_load(f)


@pytest.fixture()
def site(config):
    site = Site(address=config.get('address'), browser=config.get('browser'), sleep_time=config.get('sleep_time'))
    yield site
