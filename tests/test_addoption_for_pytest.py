import requests

'''
Проверка работы с аргументами cli pytest
'''


def test_status_code(get_url, get_statuse_code):
    response = requests.get(get_url)
    assert response.status_code == get_statuse_code
