import pytest
import requests
from jsonschema import validate
from conftest import custom_request


@pytest.mark.parametrize('resourse, count', [('posts', 100),
                                             ('comments', 500),
                                             ('albums', 100),
                                             ('photos', 5000),
                                             ('todos', 200),
                                             ('users', 10)])
def test_count_resourses(resourse, count):
    '''
    Проверка количества возвращаемых элементов
    :param resourse: имя ресурса
    :param count: количество возвращаемых элементов
    '''
    response = requests.get(f'https://jsonplaceholder.typicode.com/{resourse}')
    body = response.json()
    assert len(body) == count


def test_code_response():
    response = requests.post('https://jsonplaceholder.typicode.com/posts')
    assert response.status_code == 201


@pytest.mark.parametrize('method, endpoint, status_code', [('get', '/posts', 200),
                                                           ('get', '/posts/1', 200),
                                                           ('get', '/posts/1/comments', 200),
                                                           ('get', '/comments?postid=1', 200),
                                                           ('post', '/posts', 201),
                                                           ('put', '/posts/1', 200),
                                                           ('patch', '/posts/1', 200),
                                                           ('delete', '/posts/1', 200)
                                                           ])
def test_diferent_methods(method, endpoint, status_code):
    '''
    Проверка статус кодов для различных запросов
    '''
    response = custom_request(method, f'https://jsonplaceholder.typicode.com{endpoint}')
    assert response.status_code == status_code


@pytest.mark.parametrize('id', [1, 10, 100])
def test_id_posts(id):
    '''
    Проверка id возвращаемого поста
    :param id: номер id
    '''
    response = requests.get(f"https://jsonplaceholder.typicode.com/posts/{id}")
    body = response.json()
    assert body['id'] == id


@pytest.mark.parametrize('id', ['1', '5', '55', '100'])
def test_schema(id):
    '''
    Проверка схемы ответа для POST https://jsonplaceholder.typicode.com/posts/
    '''
    schema = {
        "type": "object",
        "properties": {
            "userId": {
                "type": "integer"
            },
            "id": {
                "type": "integer"
            },
            "title": {
                "type": "string"
            },
            "body": {
                "type": "string"
            }
        },
        "required": [
            "userId",
            "id",
            "title",
            "body"
        ]
    }
    response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{id}')
    body = response.json()
    assert validate(body, schema) == None
