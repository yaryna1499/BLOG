import requests


def test_get_articles_list():
    response = requests.get("http://nginx/api/articles")
    assert response.status_code == 200
    assert response.json()[0].get("post_id") == 3


def test_create_article():
    response = requests.post(
        "http://nginx/api/articles",
        json={"post_header": "hello", "post_text": "hello hello hello"},
    )
    assert response.status_code == 200
    assert response.json().get("post_header") == "hello"
    res = requests.delete(
        "http://nginx/api/articles/" + str(response.json().get("post_id"))
    )
    assert res.status_code == 204
