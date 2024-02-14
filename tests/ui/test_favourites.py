from litres_shop_test.helpers.application import app
import allure


@allure.title('Adding and deleting a book from favorites by an unauthorized user')
@allure.feature('Book catalog')
@allure.story('Users can manage their favorite books')
@allure.label('UI')
@allure.tag('smoke')
@allure.severity('critical')
@allure.label("owner", "Davydov")
def test_add_and_remove_book_to_favourites(browser_config):
    #ARRANGE
    app.simple_should_favourites_page.open()

    #ACT
    app.simple_should_favourites_page.search_book()
    app.simple_should_favourites_page.verify_search_results_title()
    app.simple_should_favourites_page.select_text_checkbox()
    app.simple_should_favourites_page.open_book_from_search_results()
    app.simple_should_favourites_page.verify_book_title()
    app.simple_should_favourites_page.add_book_to_favorites()
    app.simple_should_favourites_page.navigate_to_favorites_tab()
    app.simple_should_favourites_page.open_dropdown_list()
    app.simple_should_favourites_page.remove_book_from_favorites()

    #ASSERT
    app.simple_should_favourites_page.verify_book_removed_from_favorites()
