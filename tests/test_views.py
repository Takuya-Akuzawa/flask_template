from flask_package import app

def test_index():
    app.config['TESTING'] = True
    client = app.test_client()
    result = client.get('/')
    assert result.status_code == 200

def test_page_not_found():
    app.config['TESTING'] = True
    client = app.test_client()
    result = client.get('/none_page')
    assert result.status_code == 404