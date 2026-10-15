from app import app
import pytest

@pytest.fixture
def client():
    """
    Args:
    None

    Returns:
    None
    This fixture creates a test client for the Flask application, allowing us to simulate HTTP requests
    to test the application's behavior
    """
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_index_get(client):
    """
    Args:
    client: Flask test client

    Returns:
    None
    This test verifies that a GET request to the main page returns a 200 status code
    """
    response = client.get("/")
    assert response.status_code == 200


def test_index_post(client):
    """
    Args:
    client: Flask test client

    Returns:
    None
    This test verifies that a valid POST request to the main page returns the expected result
    """
    response = client.post(
        "/",
        data={"display": "5+3"}
    )
    assert response.status_code == 200
    assert b"8.0" in response.data


def test_index_post_invalid_expression(client):
    """
    Args:
    client: Flask test client

    Returns:
    None
    This test verifies that an invalid POST request to the main page returns the expected result
    """
    response = client.post(
        "/",
        data={"display": "abc+3"}
    )
    assert response.status_code == 200
    assert b"Error:" in response.data