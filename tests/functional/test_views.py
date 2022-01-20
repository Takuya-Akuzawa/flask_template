
def test_index(test_client):
    result = test_client.get('/')
    assert result.status_code == 200


def test_page_not_found(test_client):
    result = test_client.get('/none_page')
    assert result.status_code == 404