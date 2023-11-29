import pytest

from api import get

posts_path = "api/posts"
expected_title = "GRFDE"


def test_posts(config, token):
    result = get(url=f"{config['url']}/{posts_path}", token=token, params={"owner": "notMe"})
    assert result.status_code == 200
    post_titles = [post['title'] for post in result.json()['data']]
    assert expected_title in post_titles

