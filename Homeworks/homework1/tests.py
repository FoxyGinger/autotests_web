import pytest

from api import get, post

posts_path = "api/posts"
expected_title = "GRFDE"
created_post_title = "my post"
created_post_description = "post for test"
created_post_content = "some text"


def test_posts(config, token):
    """
     Тест с использованием DDT проверяет наличие поста
    с определенным заголовком в списке постов другого
    пользователя, для этого выполняется get запрос по адресу
    https://test-stand.gb.ru/api/posts c хедером, содержащим токен
    авторизации в параметре "X-Auth-Token". Для отображения
    постов другого пользователя передается "owner": "notMe"
    """
    result = get(url=f"{config['url']}/{posts_path}", token=token, params={"owner": "notMe"})
    assert result.status_code == 200
    post_titles = [post['title'] for post in result.json()['data']]
    assert expected_title in post_titles


def test_create_post(config, token):
    """
    Добавить в задание с REST API еще один
    тест, в котором создается новый пост,
    а потом проверяется его наличие на сервере
    по полю “описание”.
    """
    post_result = post(url=f"{config['url']}/{posts_path}", token=token, params={"title": created_post_title,
                                                                                 "description": created_post_description,
                                                                                 "content": created_post_content})
    assert post_result.status_code == 200
    get_result = get(url=f"{config['url']}/{posts_path}", token=token, params={"owner": "Me"})
    assert get_result.status_code == 200
    post_descriptions = [post['description'] for post in get_result.json()['data']]
    assert created_post_description in post_descriptions

