import pytest
import requests
from jsonschema import validate

'''
Тесты для эндпоинта List Breweries
'''


def test_list_breweries_status_code():
    '''
    Проверка статус кода
    '''
    response = requests.get('https://api.openbrewerydb.org/breweries')
    body = response.json()
    for breweri in body:
        print('''"''', breweri['id'], '''",''', sep='')
    assert response.status_code == 200


@pytest.mark.parametrize('city',
                         ["Boulder",
                          "Clermont",
                          "Dubuque",
                          "New Orleans",
                          "Concord",
                          "Philadelphia",
                          "Chamblee",
                          "Jackson",
                          "Hialeah",
                          "Bulverde",
                          "Radford",
                          "Houston",
                          "Pittsburgh",
                          "Northwood",
                          "Baltimore",
                          "Durango",
                          "Chardon",
                          "Lancaster",
                          "Poquoson"])
def test_list_breweries_sort_by_city(city):
    '''
    Проверка фильтрации по городу (регистронезависимая)
    '''
    response = requests.get(f'https://api.openbrewerydb.org/breweries?by_city={city}')
    body = response.json()
    for breweri in body:
        breweri_city = breweri['city']
        assert city.lower() in breweri_city.lower()


@pytest.mark.parametrize('breweri_name',
                         ["Bnaf, LLC",
                          "Boulder Beer Co",
                          "Clermont Brewing Company",
                          "Dimensional Brewing Co.",
                          "Dixie Brewing Co Inc.",
                          "Epidemic Ales",
                          "Goose Island Philadelphia",
                          "GRITS Brewing",
                          "Ironbark Brewery",
                          "King Fox Brewery",
                          "La Funke Brewing",
                          "Long Way Brewing",
                          "Mallory Brewing",
                          "Lincoln Avenue Brewery",
                          "Northwoods Brewing Co",
                          "Mobtown Brewing Co",
                          "SKA Brewing",
                          "Snow Belt Brew",
                          "Mosaic Brewing",
                          "Straight Shot Brewing"])
def test_list_breweries_sort_by_name(breweri_name):
    '''
    Проверка фильтрации по имени (регистронезависимая)
    '''
    response = requests.get(f'https://api.openbrewerydb.org/breweries?by_name={breweri_name}')
    body = response.json()
    for breweri in body:
        name = breweri['name']
        assert breweri_name.lower() in name.lower()


'''
Проверка эндпоинта Get Brewery

'''


@pytest.mark.parametrize('id', ["9094",
                                "9180",
                                "9754",
                                "10186",
                                "10217",
                                "10486",
                                "11039",
                                "11235",
                                "11767",
                                "11968",
                                "12023",
                                "12294",
                                "12459",
                                "12202",
                                "13018",
                                "12705",
                                "14347",
                                "14417",
                                "12773",
                                "14677"])
def test_get_brew_schema(id):
    schema = {
        "type": "object",
        "properties": {
            "id": {
                "type": "integer"
            },
            "obdb_id": {
                "type": "string"
            },
            "name": {
                "type": "string"
            },
            "brewery_type": {
                "type": "string"
            },
            "street": {
                "type": ["string", "null"]
            },
            "address_2": {
                "type": "null"
            },
            "address_3": {
                "type": "null"
            },
            "city": {
                "type": ["string", "null"]
            },
            "state": {
                "type": ["string", "null"]
            },
            "county_province": {
                "type": "null"
            },
            "postal_code": {
                "type": ["string", "null"]
            },
            "country": {
                "type": ["string", "null"]
            },
            "longitude": {
                "type": ["string", "null"]
            },
            "latitude": {
                "type": ["string", "null"]
            },
            "phone": {
                "type": ["string", "null"]
            },
            "website_url": {
                "type": ["string", "null"]
            },
            "updated_at": {
                "type": "string"
            },
            "created_at": {
                "type": "string"
            }
        },
        "required": [
            "id",
            "obdb_id",
            "name",
            "brewery_type",
            "address_2",
            "address_3",
            "city",
            "state",
            "county_province",
            "postal_code",
            "country",
            "longitude",
            "latitude",
            "phone",
            "website_url",
            "updated_at",
            "created_at"
        ]
    }

    response = requests.get(f'https://api.openbrewerydb.org/breweries/{id}')
    assert validate(response.json(), schema) == None
    pass


'''
Проверки для эндпоинта Search Breweries
'''


def test_search():
    response = requests.get('https://api.openbrewerydb.org/breweries/search?query=dog')
    assert response.status_code == 200
