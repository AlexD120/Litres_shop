from litres_shop_test.helpers.application import app
import allure


@allure.title('Book search functionality')
@allure.feature('Book catalog')
@allure.story('Users can search for books by title')
@allure.label('UI')
@allure.tag('smoke')
@allure.severity('critical')
@allure.label("owner", "Davydov")
def test_book_search(browser_config):
    #ARRANGE
    app.simple_should_search_page.open()

    #ACT
    app.simple_should_search_page.search_book_one()
    app.simple_should_search_page.should_search_book_one()
    app.simple_should_search_page.search_book_two()

    #ASSERT
    app.simple_should_search_page.should_search_book_two()
