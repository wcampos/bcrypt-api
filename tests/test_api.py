"""
Tests for the bcrypt API endpoints
"""
import pytest
from app.api import app

@pytest.fixture
def client():
    """Create a test client for the API"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_route(client):
    """Test the index route returns correct response"""
    response = client.get('/')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'running'
    assert data['message'] == 'Password Encryption Service'

def test_pwdncrypt_health(client):
    """Test the password encryption health check endpoint"""
    response = client.get('/pwdncrypt')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'alive'
    assert data['service'] == 'Password Encryption Service'

def test_password_encryption(client):
    """Test password encryption endpoint"""
    test_password = "testpassword123"
    response = client.get(f'/pwdncrypt/{test_password}')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'success'
    assert data['hashed_password'].startswith('$2')  # bcrypt hash prefix
    assert len(data['hashed_password']) > 50  # bcrypt hashes are typically longer than 50 chars 