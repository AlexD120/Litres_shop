import allure
from litres_shop_test.schema import schemas
from jsonschema import validate


@allure.title('Adding a book to the cart for an unauthorized user')
@allure.feature('Unauthenticated User')
@allure.story('An unauthorized user, able to add a book to the cart.')
@allure.label('API')
@allure.tag('smoke', 'regress', 'API')
@allure.severity('critical')
@allure.label("owner", "Davydov")
def test_add_book_to_cart(api_request):
    art_ids = [11220949]
    url = "/cart/arts/add"
    data = {"art_ids": art_ids}
    response = api_request(url, method='PUT', data=data)
    body = response.json()

    assert response.status_code == 200
    validate(body, schema=schemas.put_add_books_to_cart)
    assert body['payload']['data']['added_art_ids'] == art_ids
    assert body['payload']['data']['failed_art_ids'] == []
