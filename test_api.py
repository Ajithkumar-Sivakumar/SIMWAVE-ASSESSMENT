# Add sample comments to get understand.
import requests
import pytest

def test_search_api():
    api_url = "URL"
    params = {
        "duration": "30 minutes",
        "topic": "Mathematics"
    }
    response = requests.get(api_url, params=params)
    
    assert response.status_code == 200, "API request failed"
    assert "expected_value" in response.json(), "API response content is incorrect"
