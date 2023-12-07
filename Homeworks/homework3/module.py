import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


class Site:
    def __init__(self, address, browser, sleep_time=1):
        if browser == "firefox":
            service = Service(executable_path=GeckoDriverManager().install())
            options = webdriver.FirefoxOptions()
            self.driver = webdriver.Firefox(service=service, options=options)
        elif browser == "chrome":
            service = Service(executable_path=ChromeDriverManager().install())
            options = webdriver.ChromeOptions()
            self.driver = webdriver.Chrome(service=service, options=options)

        self.driver.maximize_window()  # открыть на весь экран страницу
        self.driver.get(address)  # получить адрес
        time.sleep(sleep_time)  # добавить время закрытия страницы

    def find_element(self, path, mode='xpath'):
        if mode == "css":
            mode_by = By.CSS_SELECTOR
        else:
            mode_by = By.XPATH

        return self.driver.find_element(mode_by, path)

    def get_element_property(self, mode, path, property):
        element = self.find_element(mode, path)
        return element.value_of_css_property(property)

    def close(self):
        self.driver.close()

    def wait_and_get_element(self, path, mode="xpath", timeout=5):
        if mode == "css":
            mode_by = By.CSS_SELECTOR
        else:
            mode_by = By.XPATH

        element = WebDriverWait(self.driver, timeout=timeout).until(
            expected_conditions.presence_of_element_located((mode_by, path)))

        return element
