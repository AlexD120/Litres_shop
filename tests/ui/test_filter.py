from litres_shop_test.helpers.application import app
import allure


@allure.title('Checking filter functionality in the Book Catalog')
@allure.feature('Book Catalog')
@allure.story('Users can filter books by genre, format, and language')
@allure.label('UI')
@allure.tag('smoke')
@allure.severity('medium')
@allure.label("owner", "Davydov")
def test_filter_functionality(browser_config):
    #ARRANGE
    app.simple_should_filter_page.open()

    #ACT
    app.simple_should_filter_page.open_section_new_book()
    app.simple_should_filter_page.open_directory_sport()
    app.simple_should_filter_page.select_text_checkbox()
    app.simple_should_filter_page.select_russian_language_checkbox()

    #ASSERT
    app.simple_should_filter_page.checking_title_and_selecting_checkboxes()
