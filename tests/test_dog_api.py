import pytest
import requests
from jsonschema import validate

'''
Тесты для эндпоинта https://dog.ceo/api/breeds/list/all 
'''


def test_all_breeds_code(request_all_breeds):
    """
    Проверка статус кода
    """
    res = request_all_breeds
    assert res.status_code == 200


def test_all_breeds_scheme(request_all_breeds):
    """
    Проверка схемы ответа
    """
    res = request_all_breeds
    schema = {
        "type": "object",
        "properties": {
            "message": {
                "type": "object",
                "properties": {
                    "affenpinscher": {
                        "type": "array",
                        "items": {}
                    },
                    "african": {
                        "type": "array",
                        "items": {}
                    },
                    "airedale": {
                        "type": "array",
                        "items": {}
                    },
                    "akita": {
                        "type": "array",
                        "items": {}
                    },
                    "appenzeller": {
                        "type": "array",
                        "items": {}
                    },
                    "australian": {
                        "type": "array",
                        "items": [
                            {
                                "type": "string"
                            }
                        ]
                    },
                    "basenji": {
                        "type": "array",
                        "items": {}
                    },
                    "beagle": {
                        "type": "array",
                        "items": {}
                    },
                    "bluetick": {
                        "type": "array",
                        "items": {}
                    },
                    "borzoi": {
                        "type": "array",
                        "items": {}
                    },
                    "bouvier": {
                        "type": "array",
                        "items": {}
                    },
                    "boxer": {
                        "type": "array",
                        "items": {}
                    },
                    "brabancon": {
                        "type": "array",
                        "items": {}
                    },
                    "briard": {
                        "type": "array",
                        "items": {}
                    },
                    "buhund": {
                        "type": "array",
                        "items": [
                            {
                                "type": "string"
                            }
                        ]
                    },
                    "bulldog": {
                        "type": "array",
                        "items": [
                            {
                                "type": "string"
                            },
                            {
                                "type": "string"
                            },
                            {
                                "type": "string"
                            }
                        ]
                    },
                    "bullterrier": {
                        "type": "array",
                        "items": [
                            {
                                "type": "string"
                            }
                        ]
                    },
                    "cattledog": {
                        "type": "array",
                        "items": [
                            {
                                "type": "string"
                            }
                        ]
                    },
                    "chihuahua": {
                        "type": "array",
                        "items": {}
                    },
                    "chow": {
                        "type": "array",
                        "items": {}
                    },
                    "clumber": {
                        "type": "array",
                        "items": {}
                    },
                    "cockapoo": {
                        "type": "array",
                        "items": {}
                    },
                    "collie": {
                        "type": "array",
                        "items": [
                            {
                                "type": "string"
                            }
                        ]
                    },
                    "coonhound": {
                        "type": "array",
                        "items": {}
                    },
                    "corgi": {
                        "type": "array",
                        "items": [
                            {
                                "type": "string"
                            }
                        ]
                    },
                    "cotondetulear": {
                        "type": "array",
                        "items": {}
                    },
                    "dachshund": {
                        "type": "array",
                        "items": {}
                    },
                    "dalmatian": {
                        "type": "array",
                        "items": {}
                    },
                    "dane": {
                        "type": "array",
                        "items": [
                            {
                                "type": "string"
                            }
                        ]
                    },
                    "deerhound": {
                        "type": "array",
                        "items": [
                            {
                                "type": "string"
                            }
                        ]
                    },
                    "dhole": {
                        "type": "array",
                        "items": {}
                    },
                    "dingo": {
                        "type": "array",
                        "items": {}
                    },
                    "doberman": {
                        "type": "array",
                        "items": {}
                    },
                    "elkhound": {
                        "type": "array",
                        "items": [
                            {
                                "type": "string"
                            }
                        ]
                    },
                    "entlebucher": {
                        "type": "array",
                        "items": {}
                    },
                    "eskimo": {
                        "type": "array",
                        "items": {}
                    },
                    "finnish": {
                        "type": "array",
                        "items": [
                            {
                                "type": "string"
                            }
                        ]
                    },
                    "frise": {
                        "type": "array",
                        "items": [
                            {
                                "type": "string"
                            }
                        ]
                    },
                    "germanshepherd": {
                        "type": "array",
                        "items": {}
                    },
                    "greyhound": {
                        "type": "array",
                        "items": [
                            {
                                "type": "string"
                            }
                        ]
                    },
                    "groenendael": {
                        "type": "array",
                        "items": {}
                    },
                    "havanese": {
                        "type": "array",
                        "items": {}
                    },
                    "hound": {
                        "type": "array",
                        "items": [
                            {
                                "type": "string"
                            },
                            {
                                "type": "string"
                            },
                            {
                                "type": "string"
                            },
                            {
                                "type": "string"
                            },
                            {
                                "type": "string"
                            },
                            {
                                "type": "string"
                            },
                            {
                                "type": "string"
                            }
                        ]
                    },
                    "husky": {
                        "type": "array",
                        "items": {}
                    },
                    "keeshond": {
                        "type": "array",
                        "items": {}
                    },
                    "kelpie": {
                        "type": "array",
                        "items": {}
                    },
                    "komondor": {
                        "type": "array",
                        "items": {}
                    },
                    "kuvasz": {
                        "type": "array",
                        "items": {}
                    },
                    "labradoodle": {
                        "type": "array",
                        "items": {}
                    },
                    "labrador": {
                        "type": "array",
                        "items": {}
                    },
                    "leonberg": {
                        "type": "array",
                        "items": {}
                    },
                    "lhasa": {
                        "type": "array",
                        "items": {}
                    },
                    "malamute": {
                        "type": "array",
                        "items": {}
                    },
                    "malinois": {
                        "type": "array",
                        "items": {}
                    },
                    "maltese": {
                        "type": "array",
                        "items": {}
                    },
                    "mastiff": {
                        "type": "array",
                        "items": [
                            {
                                "type": "string"
                            },
                            {
                                "type": "string"
                            },
                            {
                                "type": "string"
                            }
                        ]
                    },
                    "mexicanhairless": {
                        "type": "array",
                        "items": {}
                    },
                    "mix": {
                        "type": "array",
                        "items": {}
                    },
                    "mountain": {
                        "type": "array",
                        "items": [
                            {
                                "type": "string"
                            },
                            {
                                "type": "string"
                            }
                        ]
                    },
                    "newfoundland": {
                        "type": "array",
                        "items": {}
                    },
                    "otterhound": {
                        "type": "array",
                        "items": {}
                    },
                    "ovcharka": {
                        "type": "array",
                        "items": [
                            {
                                "type": "string"
                            }
                        ]
                    },
                    "papillon": {
                        "type": "array",
                        "items": {}
                    },
                    "pekinese": {
                        "type": "array",
                        "items": {}
                    },
                    "pembroke": {
                        "type": "array",
                        "items": {}
                    },
                    "pinscher": {
                        "type": "array",
                        "items": [
                            {
                                "type": "string"
                            }
                        ]
                    },
                    "pitbull": {
                        "type": "array",
                        "items": {}
                    },
                    "pointer": {
                        "type": "array",
                        "items": [
                            {
                                "type": "string"
                            },
                            {
                                "type": "string"
                            }
                        ]
                    },
                    "pomeranian": {
                        "type": "array",
                        "items": {}
                    },
                    "poodle": {
                        "type": "array",
                        "items": [
                            {
                                "type": "string"
                            },
                            {
                                "type": "string"
                            },
                            {
                                "type": "string"
                            }
                        ]
                    },
                    "pug": {
                        "type": "array",
                        "items": {}
                    },
                    "puggle": {
                        "type": "array",
                        "items": {}
                    },
                    "pyrenees": {
                        "type": "array",
                        "items": {}
                    },
                    "redbone": {
                        "type": "array",
                        "items": {}
                    },
                    "retriever": {
                        "type": "array",
                        "items": [
                            {
                                "type": "string"
                            },
                            {
                                "type": "string"
                            },
                            {
                                "type": "string"
                            },
                            {
                                "type": "string"
                            }
                        ]
                    },
                    "ridgeback": {
                        "type": "array",
                        "items": [
                            {
                                "type": "string"
                            }
                        ]
                    },
                    "rottweiler": {
                        "type": "array",
                        "items": {}
                    },
                    "saluki": {
                        "type": "array",
                        "items": {}
                    },
                    "samoyed": {
                        "type": "array",
                        "items": {}
                    },
                    "schipperke": {
                        "type": "array",
                        "items": {}
                    },
                    "schnauzer": {
                        "type": "array",
                        "items": [
                            {
                                "type": "string"
                            },
                            {
                                "type": "string"
                            }
                        ]
                    },
                    "setter": {
                        "type": "array",
                        "items": [
                            {
                                "type": "string"
                            },
                            {
                                "type": "string"
                            },
                            {
                                "type": "string"
                            }
                        ]
                    },
                    "sheepdog": {
                        "type": "array",
                        "items": [
                            {
                                "type": "string"
                            },
                            {
                                "type": "string"
                            }
                        ]
                    },
                    "shiba": {
                        "type": "array",
                        "items": {}
                    },
                    "shihtzu": {
                        "type": "array",
                        "items": {}
                    },
                    "spaniel": {
                        "type": "array",
                        "items": [
                            {
                                "type": "string"
                            },
                            {
                                "type": "string"
                            },
                            {
                                "type": "string"
                            },
                            {
                                "type": "string"
                            },
                            {
                                "type": "string"
                            },
                            {
                                "type": "string"
                            },
                            {
                                "type": "string"
                            }
                        ]
                    },
                    "springer": {
                        "type": "array",
                        "items": [
                            {
                                "type": "string"
                            }
                        ]
                    },
                    "stbernard": {
                        "type": "array",
                        "items": {}
                    },
                    "terrier": {
                        "type": "array",
                        "items": [
                            {
                                "type": "string"
                            },
                            {
                                "type": "string"
                            },
                            {
                                "type": "string"
                            },
                            {
                                "type": "string"
                            },
                            {
                                "type": "string"
                            },
                            {
                                "type": "string"
                            },
                            {
                                "type": "string"
                            },
                            {
                                "type": "string"
                            },
                            {
                                "type": "string"
                            },
                            {
                                "type": "string"
                            },
                            {
                                "type": "string"
                            },
                            {
                                "type": "string"
                            },
                            {
                                "type": "string"
                            },
                            {
                                "type": "string"
                            },
                            {
                                "type": "string"
                            },
                            {
                                "type": "string"
                            },
                            {
                                "type": "string"
                            },
                            {
                                "type": "string"
                            },
                            {
                                "type": "string"
                            },
                            {
                                "type": "string"
                            },
                            {
                                "type": "string"
                            },
                            {
                                "type": "string"
                            }
                        ]
                    },
                    "vizsla": {
                        "type": "array",
                        "items": {}
                    },
                    "waterdog": {
                        "type": "array",
                        "items": [
                            {
                                "type": "string"
                            }
                        ]
                    },
                    "weimaraner": {
                        "type": "array",
                        "items": {}
                    },
                    "whippet": {
                        "type": "array",
                        "items": {}
                    },
                    "wolfhound": {
                        "type": "array",
                        "items": [
                            {
                                "type": "string"
                            }
                        ]
                    }
                },
                "required": [
                    "affenpinscher",
                    "african",
                    "airedale",
                    "akita",
                    "appenzeller",
                    "australian",
                    "basenji",
                    "beagle",
                    "bluetick",
                    "borzoi",
                    "bouvier",
                    "boxer",
                    "brabancon",
                    "briard",
                    "buhund",
                    "bulldog",
                    "bullterrier",
                    "cattledog",
                    "chihuahua",
                    "chow",
                    "clumber",
                    "cockapoo",
                    "collie",
                    "coonhound",
                    "corgi",
                    "cotondetulear",
                    "dachshund",
                    "dalmatian",
                    "dane",
                    "deerhound",
                    "dhole",
                    "dingo",
                    "doberman",
                    "elkhound",
                    "entlebucher",
                    "eskimo",
                    "finnish",
                    "frise",
                    "germanshepherd",
                    "greyhound",
                    "groenendael",
                    "havanese",
                    "hound",
                    "husky",
                    "keeshond",
                    "kelpie",
                    "komondor",
                    "kuvasz",
                    "labradoodle",
                    "labrador",
                    "leonberg",
                    "lhasa",
                    "malamute",
                    "malinois",
                    "maltese",
                    "mastiff",
                    "mexicanhairless",
                    "mix",
                    "mountain",
                    "newfoundland",
                    "otterhound",
                    "ovcharka",
                    "papillon",
                    "pekinese",
                    "pembroke",
                    "pinscher",
                    "pitbull",
                    "pointer",
                    "pomeranian",
                    "poodle",
                    "pug",
                    "puggle",
                    "pyrenees",
                    "redbone",
                    "retriever",
                    "ridgeback",
                    "rottweiler",
                    "saluki",
                    "samoyed",
                    "schipperke",
                    "schnauzer",
                    "setter",
                    "sheepdog",
                    "shiba",
                    "shihtzu",
                    "spaniel",
                    "springer",
                    "stbernard",
                    "terrier",
                    "vizsla",
                    "waterdog",
                    "weimaraner",
                    "whippet",
                    "wolfhound"
                ]
            },
            "status": {
                "type": "string"
            }
        },
        "required": [
            "message",
            "status"
        ]
    }
    assert validate(instance=res.json(), schema=schema) == None


def test_all_dreeds_bad_requests():
    '''
    Проверка статус кода при неправильном запросе
    '''
    res = requests.post("https://dog.ceo/api/breeds/list/all")
    assert res.status_code == 405


def test_all_breeeds_error_masage():
    '''
        Проверка возвращаемого error message при неправвильном запросе
    '''
    res = requests.put("https://dog.ceo/api/breeds/list/all")
    response = res.json()
    message = '''No route found for "PUT /api/breeds/list/all": Method Not Allowed (Allow: GET, HEAD) with code: 0'''
    assert response["message"] == message


'''
Тесты для эндпоинта https://dog.ceo/api/breeds/image/random
'''


def test_dogs_image():
    '''
    Проверка статус кода с правильным запросом
    '''
    res = requests.get("https://dog.ceo/api/breeds/image/random")
    assert res.status_code == 200


def test_dogs_image_random():
    '''
    Проверка рандомности картинок
    '''

    res1 = requests.get("https://dog.ceo/api/breeds/image/random")
    image1 = res1.content
    res2 = requests.get("https://dog.ceo/api/breeds/image/random")
    image2 = res2.content
    assert image1 != image2


def test_dogs_image_scheme():
    '''
    Проверка схемы ответа
    '''

    res = requests.get("https://dog.ceo/api/breeds/image/random")
    schema = {
        "type": "object",
        "properties": {
            "message": {
                "type": "string"
            },
            "status": {
                "type": "string"
            }
        },
        "required": [
            "message",
            "status"
        ]
    }

    assert validate(res.json(), schema) == None


@pytest.mark.parametrize('count_in_request, count_images',
                         [('0', 1),
                          ('1', 1),
                          ('25', 25),
                          ('50', 50),
                          ('51', 50),
                          ('100', 50)])
def test_count_dogs_images(count_in_request, count_images):
    '''
    Проверка колличества возвращаемых изображений
    '''
    res = requests.get(f"https://dog.ceo/api/breeds/image/random/{count_in_request}")
    body = res.json()
    assert len(body["message"]) == count_images


'''
Тесты для эндпоинта https://dog.ceo/api/breed/hound/images
'''


def test_count_images_by_breed():
    '''
    Проверка колличества всех возвращаемых изображений
    '''
    res = requests.get("https://dog.ceo/api/breed/hound/images")
    body = res.json()
    assert len(body["message"]) == 1000


def test_schema_random_images_by_breed():
    '''
    Проверка схемы ответа
    '''

    res = requests.get("https://dog.ceo/api/breed/hound/images/random")
    schema = {
        "type": "object",
        "properties": {
            "message": {
                "type": "string"
            },
            "status": {
                "type": "string"
            }
        },
        "required": [
            "message",
            "status"
        ]
    }

    assert validate(res.json(), schema) == None


@pytest.mark.parametrize('count_in_request, count_images',
                         [('0', 1),
                          ('1', 1),
                          ('25', 25),
                          ('50', 50),
                          ('51', 51),
                          ('100', 100)])
def test_count_dogs_images_random_by_breed(count_in_request, count_images):
    '''
    Проверка колличества возвращаемых изображений
    '''
    res = requests.get(f"https://dog.ceo/api/breed/hound/images/random/{count_in_request}")
    body = res.json()
    assert len(body["message"]) == count_images


'''
Тесты для эндпоинта https://dog.ceo/api/breed/hound/list
'''


@pytest.mark.parametrize('sub_breed, count_images',
                         [("afghan", 239),
                          ("basset", 175),
                          ("blood", 187),
                          ("english", 157),
                          ("ibizan", 188),
                          ("plott", 2),
                          ("walker", 153)])
def test_count_dogs_images_by_sub_breed(sub_breed, count_images):
    '''
    Проверка колличества возвращаемых изображений для разных пород
    '''
    res = requests.get(f"https://dog.ceo/api/breed/hound/{sub_breed}/images")
    body = res.json()
    assert len(body["message"]) == count_images
