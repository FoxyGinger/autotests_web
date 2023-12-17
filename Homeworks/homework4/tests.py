import logging
import time

from api import get, post


def test_step1(test_page):
    logging.info("Test 1 Starting")
    test_page.go_to_site()
    test_page.enter_login("test")
    test_page.enter_pass("test")
    test_page.click_login_button()
    assert test_page.get_error_text() == "401"


def test_step2(test_page, test_data):
    logging.info("Test 2 Starting")
    test_page.go_to_site()
    test_page.enter_login(test_data["login"])
    test_page.enter_pass(test_data["password"])
    test_page.click_login_button()
    assert test_page.get_text_blog() == "Blog"


def test_step3(test_page, test_data):
    # 1 login
    logging.info("Test 3 Starting")
    test_page.go_to_site()
    test_page.enter_login(test_data["login"])
    test_page.enter_pass(test_data["password"])
    test_page.click_login_button()
    assert test_page.get_text_blog() == "Blog"

    # 2 create new post
    time.sleep(1)
    test_page.click_new_post()
    time.sleep(1)
    new_post_title_expected = "test post title"
    test_page.enter_new_post_title(new_post_title_expected)
    time.sleep(1)
    test_page.click_save_new_post()

    # 3 check new post
    time.sleep(1)
    assert test_page.get_post_title() == new_post_title_expected


def test_step4(test_page, test_data, email_report):
    logging.info("Test 4 Starting")
    test_page.go_to_site()

    # 1 login
    logging.info("1. Login")
    test_page.enter_login(test_data["login"])
    test_page.enter_pass(test_data["password"])
    test_page.click_login_button()
    assert test_page.get_text_blog() == "Blog"

    # 2 Contact
    logging.info("2. Contact")
    test_page.click_contact_button()
    time.sleep(1)

    # 3 Fill form
    logging.info("3. Fill form")
    test_page.enter_contact_name("Tester")
    test_page.enter_contact_email("some_email@test.com")
    test_page.enter_contact_content("some text")
    test_page.click_contact_contact_us_button()
    time.sleep(1)

    # 4 Check alert
    logging.info("4. Check alert")
    assert test_page.get_alert_text() == "Form successfully submitted"


def test_posts(test_data, token):
    """
     Тест с использованием DDT проверяет наличие поста
    с определенным заголовком в списке постов другого
    пользователя, для этого выполняется get запрос по адресу
    https://test-stand.gb.ru/api/posts c хедером, содержащим токен
    авторизации в параметре "X-Auth-Token". Для отображения
    постов другого пользователя передается "owner": "notMe"
    """
    logging.info('test_posts starting')
    assert token, "token is missing"
    response = get(url=f"{test_data['address']}/{test_data['posts_path']}", token=token, params={"owner": "notMe"})
    assert response, "invalid response"
    expected_title = "K0ZF6"
    post_titles = [post['title'] for post in response.json()['data']]
    assert expected_title in post_titles


def test_create_post(test_data, token):
    """
    Добавить в задание с REST API еще один
    тест, в котором создается новый пост,
    а потом проверяется его наличие на сервере
    по полю “описание”.
    """
    logging.info('test_create_post starting')
    created_post_title = "my post"
    created_post_description = "post for test"
    created_post_content = "some text"
    post_response = post(url=f"{test_data['address']}/{test_data['posts_path']}", token=token, params={"title": created_post_title,
                                                                                 "description": created_post_description,
                                                                                 "content": created_post_content})
    assert post_response, "invalid response"
    get_response = get(url=f"{test_data['address']}/{test_data['posts_path']}", token=token, params={"owner": "Me"})
    assert get_response, "invalid response"
    post_descriptions = [post['description'] for post in get_response.json()['data']]
    assert created_post_description in post_descriptions