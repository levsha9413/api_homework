import pytest
import requests


@pytest.fixture(scope="session")
def request_all_breeds():
    response = requests.get("https://dog.ceo/api/breeds/list/all")
    return response


def custom_request(method, url):
    if method == 'post':
        rez = requests.post(url)
    elif method == 'get':
        rez = requests.get(url)
    elif method == 'put':
        rez = requests.put(url)
    elif method == 'patch':
        rez = requests.patch(url)
    elif method == 'delete':
        rez = requests.delete(url)
    else:
        raise AttributeError(f"Excpected method = ['post'|'get'|'put'|'patch','delete'], but recived method = {method}")
    return rez


'''
Добавление аргументов cli для pytest:
'''


def pytest_addoption(parser):
    parser.addoption(
        "--url", default="https://ya.ru"
    )
    parser.addoption(
        "--status_code", default=200, type=int
    )


@pytest.fixture
def get_url(request):
    return request.config.getoption("--url")


@pytest.fixture
def get_statuse_code(request):
    return request.config.getoption("--status_code")
