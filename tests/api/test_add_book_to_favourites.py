import allure


@allure.title('Adding a book to favorites via API')
@allure.feature('API Operations')
@allure.story('User to add a specific book to my favorites.')
@allure.label('API')
@allure.tag('smoke', 'regress', 'API')
@allure.severity('critical')
@allure.label("owner", "Davydov")
def test_add_book_to_favorites(api_request):
    url = "/wishlist/arts/12928406"

    response = api_request(url, method='PUT')

    assert response.status_code == 204
    assert response.text == ""
