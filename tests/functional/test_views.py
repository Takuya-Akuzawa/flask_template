"""
This file (test_views.py) contains the functional tests for the `views` blueprint.

These tests use GETs and POSTs to different URLs to check for the proper behavior
of the `views` blueprint.
"""


def test_index(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is requested (GET)
    THEN check the response is valid
    """
    response = test_client.get('/')
    assert response.status_code == 200
    assert b'Index' in response.data


def test_page_not_found(test_client):
    """
    GIVEN
    WHEN
    THEN
    """
    response = test_client.get('/none_page')
    assert response.status_code == 404
    assert 'リクエストされたページが見つかりませんでした。'.encode() in response.data