from litres_shop_test.helpers.application import app
import allure


@allure.title('Add and remove a book from the cart')
@allure.feature('Book catalog')
@allure.story('Users can manage books in their cart')
@allure.label('UI')
@allure.tag('smoke')
@allure.severity('critical')
@allure.label("owner", "Davydov")
def test_add_and_remove_book_to_cart(browser_config):
    #ARRANGE
    app.simple_should_cart_page.open()

    #ACT
    app.simple_should_cart_page.search_book()
    app.simple_should_cart_page.verify_search_results_title()
    app.simple_should_cart_page.select_text_checkbox()
    app.simple_should_cart_page.open_book_from_search_results()
    app.simple_should_cart_page.verify_book_title()
    app.simple_should_cart_page.add_book_to_cart()
    app.simple_should_cart_page.navigate_to_cart_tab()
    app.simple_should_cart_page.verify_book_in_cart()
    app.simple_should_cart_page.remove_book_from_cart()

    #ASSERT
    app.simple_should_cart_page.verify_book_removed_from_cart()
