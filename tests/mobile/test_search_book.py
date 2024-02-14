import allure
from litres_shop_test.helpers.application import app_mobile
from litres_shop_test.helpers.skip_onboarding import skip_onboarding_question


@allure.title("Search for a book and verify title")
@allure.feature("Simple Search")
@allure.story("Successful search")
@allure.label("UI")
@allure.tag("smoke")
@allure.severity("critical")
@allure.label("owner", "Davydov")
def test_search_book():
    #ARRANGE
    skip_onboarding_question()

    #ACT
    app_mobile.simple_search_book_page.search()

    #ASSERT
    app_mobile.simple_search_book_page.verify_book_title()
