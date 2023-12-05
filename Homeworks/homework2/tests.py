import time


def test_step1(site, login_xpath, password_xpath, login_button_xpath, login_error_xpath):
    input1 = site.find_element(login_xpath)
    input1.send_keys("test")
    input2 = site.find_element(password_xpath)
    input2.send_keys("test")
    button = site.find_element(login_button_xpath)
    button.click()
    error_label = site.wait_and_get_element(login_error_xpath)
    assert error_label.text == "401"


def test_step2(site, test_data, login_xpath, password_xpath, login_button_xpath, login_success_xpath):
    input1 = site.find_element(login_xpath)
    input1.send_keys(test_data["login"])
    input2 = site.find_element(password_xpath)
    input2.send_keys(test_data["password"])
    button = site.find_element(login_button_xpath)
    button.click()
    login_success = site.wait_and_get_element(login_success_xpath)
    assert login_success.text == "Blog"
