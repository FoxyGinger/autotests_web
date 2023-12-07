from base_page import BasePage
from selenium.webdriver.common.by import By


class TestSearchLocators:
    LOCATOR_LOGIN_FIELD = (By.XPATH, """//*[@id="login"]/div[1]/label/input""")
    LOCATOR_PASS_FIELD = (By.XPATH, """//*[@id="login"]/div[2]/label/input""")
    LOCATOR_LOGIN_BTN = (By.CSS_SELECTOR, "button")
    LOCATOR_ERROR_FIELD = (By.XPATH, """//*[@id="app"]/main/div/div/div[2]/h2""")
    LOCATOR_LOGIN_RESULT = (By.XPATH, """//*[@id="app"]/main/div/div[1]/h1""")
    LOCATOR_NEW_POST_BTN = (By.XPATH, """//*[@id="create-btn"]""")
    LOCATOR_NEW_POST_TITLE_FIELD = (By.XPATH, """//*[@id="create-item"]/div/div/div[1]/div/label/input""")
    LOCATOR_NEW_POST_SAVE_BTN = (By.XPATH, """//*[@id="create-item"]/div/div/div[7]/div/button""")
    LOCATOR_POST_TITLE_FIELD = (By.XPATH, """//*[@id="app"]/main/div/div[1]/h1""")


class OperationsHelper(BasePage):
    def enter_login(self, word):
        login_field = self.find_element(TestSearchLocators.LOCATOR_LOGIN_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def enter_pass(self, word):
        pass_field = self.find_element(TestSearchLocators.LOCATOR_PASS_FIELD)
        pass_field.clear()
        pass_field.send_keys(word)

    def click_login_button(self):
        self.find_element(TestSearchLocators.LOCATOR_LOGIN_BTN).click()

    def get_error_text(self):
        error_field = self.find_element(TestSearchLocators.LOCATOR_ERROR_FIELD, timeout=2)
        return error_field.text

    def get_text_blog(self):
        blog_field = self.find_element(TestSearchLocators.LOCATOR_LOGIN_RESULT, timeout=2)
        return blog_field.text

    def click_new_post(self):
        self.find_element(TestSearchLocators.LOCATOR_NEW_POST_BTN).click()

    def enter_new_post_title(self, word):
        title_field = self.find_element(TestSearchLocators.LOCATOR_NEW_POST_TITLE_FIELD)
        title_field.clear()
        title_field.send_keys(word)

    def click_save_new_post(self):
        self.find_element(TestSearchLocators.LOCATOR_NEW_POST_SAVE_BTN).click()

    def get_post_title(self):
        title_field = self.find_element(TestSearchLocators.LOCATOR_POST_TITLE_FIELD, timeout=2)
        return title_field.text
