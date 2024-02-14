import allure

from litres_shop_test.schema import schemas
from jsonschema import validate


@allure.title('Verify successful book search by title and type')
@allure.feature('Book Search')
@allure.story('Search books by title and type')
@allure.label('API')
@allure.tag('smoke', 'regress', 'API', 'registration')
@allure.severity('critical')
@allure.label("owner", "Davydov")
def test_get_search_book(api_request):
    book_title = 'Франк Тилье Головоломка'
    art_types = 'text_book'
    types = 'text_book'
    url = f"/search?q={book_title}&art_types={art_types}&types={types}"
    response = api_request(url)
    body = response.json()

    assert response.status_code == 200
    validate(body, schema=schemas.get_search_book)
    assert body['payload']['data'][0]['instance']['title'] == 'Головоломка'
    assert body['payload']['data'][0]['type'] == 'text_book'
    assert body['payload']['data'][0]['instance']['persons'][0]['full_name'] == 'Франк Тилье'
