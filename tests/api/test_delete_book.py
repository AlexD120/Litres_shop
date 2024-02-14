import allure


@allure.title('Delete a specific book to my favorites via API')
@allure.feature('API Operations')
@allure.story('Delete a specific book to my favorites.')
@allure.label('API')
@allure.tag('smoke', 'regress', 'API')
@allure.severity('critical')
@allure.label("owner", "Davydov")
def test_delete_book_from_favorite(api_request):
    url = "/wishlist/arts/70330762"
    headers = {
        'wishlist': '70330762'
    }
    response = api_request(url, method='DELETE', headers=headers)

    assert response.status_code == 204
    assert response.text == ''