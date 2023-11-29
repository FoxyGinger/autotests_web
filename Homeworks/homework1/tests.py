import pytest

from api import get, post

posts_path = "api/posts"
expected_title = "GRFDE"
created_post_title = "my post"
created_post_description = "post for test"
created_post_content = "some text"


def test_posts(config, token):
    result = get(url=f"{config['url']}/{posts_path}", token=token, params={"owner": "notMe"})
    assert result.status_code == 200
    post_titles = [post['title'] for post in result.json()['data']]
    assert expected_title in post_titles


def test_create_post(config, token):
    post_result = post(url=f"{config['url']}/{posts_path}", token=token, params={"title": created_post_title,
                                                                                 "description": created_post_description,
                                                                                 "content": created_post_content})
    assert post_result.status_code == 200
    get_result = get(url=f"{config['url']}/{posts_path}", token=token, params={"owner": "Me"})
    assert get_result.status_code == 200
    post_descriptions = [post['description'] for post in get_result.json()['data']]
    assert created_post_description in post_descriptions

