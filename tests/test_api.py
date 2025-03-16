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
    assert b"Hey buddy!" in response.data

def test_pwdncrypt_health(client):
    """Test the password encryption health check endpoint"""
    response = client.get('/pwdncrypt')
    assert response.status_code == 200
    assert b"Password Encryption Service -- ALIVE!" in response.data

def test_password_encryption(client):
    """Test password encryption endpoint"""
    test_password = "testpassword123"
    response = client.get(f'/pwdncrypt/{test_password}')
    assert response.status_code == 200
    # Check if response is a valid bcrypt hash
    assert response.data.startswith(b'$2')
    assert len(response.data) > 50  # bcrypt hashes are typically longer than 50 chars 