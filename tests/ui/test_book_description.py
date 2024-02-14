from litres_shop_test.helpers.application import app
import allure


@allure.title('Get book description')
@allure.feature('Book catalog')
@allure.story('Users can view book descriptions')
@allure.label('UI')
@allure.tag('smoke')
@allure.severity('minor')
@allure.label("owner", "Davydov")
def test_description_book(browser_config):
    #ARRANGE
    app.simple_should_book_description.open()

    #ACT
    app.simple_should_book_description.search_book()
    app.simple_should_book_description.verify_search_results_title()
    app.simple_should_book_description.select_text_checkbox()
    app.simple_should_book_description.open_book_from_search_results()

    #ASSERT
    app.simple_should_book_description.verify_book_title()
    app.simple_should_book_description.verify_author_name()
    app.simple_should_book_description.verify_book_description()
