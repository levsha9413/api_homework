import pytest
import requests


@pytest.fixture(scope="session")
def request_all_breeds():
    response = requests.get("https://dog.ceo/api/breeds/list/all")
    return response
