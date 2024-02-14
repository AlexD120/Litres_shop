from litres_shop_test.helpers.application import app
import allure


@allure.title('Checking the navigation and display of the catalog')
@allure.feature('Book Catalog')
@allure.story('Users can view and open sections of the catalog')
@allure.label('UI')
@allure.tag('smoke')
@allure.severity('medium')
@allure.label("owner", "Davydov")
def test_navigation_of_the_catalog(browser_config):
    #ARRANGE
    app.simple_should_catalog_page.open()

    #ACT
    app.simple_should_catalog_page.open_catalog_hobby()
    app.simple_should_catalog_page.should_directory_section_hobby()
    app.simple_should_catalog_page.open_catalog_skills()
    app.simple_should_catalog_page.should_directory_section_skills()
    app.simple_should_catalog_page.open_catalog_serious_reading()

    #ASSERT
    app.simple_should_catalog_page.should_directory_section_serious_reading()
