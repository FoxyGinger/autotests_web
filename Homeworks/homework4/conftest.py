import logging

import pytest
import requests
import yaml

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from testpage import OperationsHelper
from email_report import send_email


@pytest.fixture(scope="session")
def test_data() -> dict:
    with open('test_data.yaml') as f:
        return yaml.safe_load(f)


@pytest.fixture(scope="session")
def browser(test_data):
    if test_data.get('browser') == "firefox":
        service = Service(executable_path=GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=service, options=options)
    else:
        service = Service(executable_path=ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


@pytest.fixture()
def test_page(browser, test_data):
    yield OperationsHelper(browser, test_data.get('address'))


@pytest.fixture(scope="session")
def email_report():
    yield
    send_email()


@pytest.fixture(scope="session")
def token(test_data):
    logging.debug('Отправка запроса для токена')
    try:
        response = requests.post(url=f"{test_data['address']}/{test_data['login_path']}", data={"username": test_data['login'], "password": test_data['password']})
    except:
        logging.exception(f'Exception while get token')
        return None

    if response.status_code != 200:
        logging.error(f"Can't get token: {response.text}")
        return None

    return response.json()['token']