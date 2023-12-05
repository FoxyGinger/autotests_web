import pytest
import yaml

from module import Site


@pytest.fixture()
def test_data() -> dict:
    with open('test_data.yaml') as f:
        return yaml.safe_load(f)


@pytest.fixture()
def site(test_data):
    site = Site(address=test_data.get('address'), browser=test_data.get('browser'),
                sleep_time=test_data.get('sleep_time'))
    yield site
    site.close()


@pytest.fixture()
def login_xpath():
    return """//*[@id="login"]/div[1]/label/input"""


@pytest.fixture()
def password_xpath():
    return """//*[@id="login"]/div[2]/label/input"""


@pytest.fixture()
def login_button_xpath():
    return """//*[@id="login"]/div[3]/button"""


@pytest.fixture()
def login_error_xpath():
    return """//*[@id="app"]/main/div/div/div[2]/h2"""


@pytest.fixture()
def login_success_xpath():
    return """//*[@id="app"]/main/div/div[1]/h1"""


