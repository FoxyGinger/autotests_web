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


def test_step3(site, test_data, login_xpath, password_xpath, login_button_xpath, login_success_xpath,
               new_post_button_xpath, new_post_title_input_xpath, new_post_save_button_xpath,
               new_post_title_xpath):
    # 1 login
    input1 = site.find_element(login_xpath)
    input1.send_keys(test_data["login"])
    input2 = site.find_element(password_xpath)
    input2.send_keys(test_data["password"])
    button = site.find_element(login_button_xpath)
    button.click()
    login_success = site.wait_and_get_element(login_success_xpath)
    assert login_success.text == "Blog"

    # 2 create new post
    time.sleep(1)
    post_button = site.find_element(new_post_button_xpath)
    post_button.click()
    time.sleep(1)
    new_post_title_expected = "test post title"
    title_input = site.wait_and_get_element(new_post_title_input_xpath)
    title_input.send_keys(new_post_title_expected)
    save_post_button = site.find_element(new_post_save_button_xpath)
    save_post_button.click()

    # 3 check new post
    time.sleep(1)
    new_post_title_actual = site.find_element(new_post_title_xpath).text
    assert new_post_title_actual == new_post_title_expected
