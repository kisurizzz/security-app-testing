import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    """Test that home page loads successfully"""
    rv = client.get('/')
    assert rv.status_code == 200

def test_search_endpoint(client):
    """Test the search endpoint"""
    rv = client.get('/search?query=test')
    assert rv.status_code == 200

def test_login_page(client):
    """Test that login page loads successfully"""
    rv = client.get('/login')
    assert rv.status_code == 200
