import allure
from litres_shop_test.helpers.application import app_mobile
from litres_shop_test.helpers.skip_onboarding import skip_onboarding_question


@allure.title("End-to-End User Flow")
@allure.feature("User Authorization and Book Management")
@allure.story(
    "As a user, I want to authorize, search for a book, add it to favorites, view and manage saved books."
)
@allure.label("UI")
@allure.tag("smoke")
@allure.severity("critical")
@allure.label("owner", "Davydov")
def test_add_book_to_cart():
    # ARRANGE
    skip_onboarding_question()
    app_mobile.simple_user_authorization_page.account()
    app_mobile.simple_user_authorization_page.authorization_account()
    app_mobile.simple_user_authorization_page.skip_number_notifications()

    # ACT
    app_mobile.simple_search_book_page.search()
    app_mobile.simple_search_book_page.verify_book_title()
    app_mobile.simple_user_save_book.add_to_favorites()
    app_mobile.simple_user_save_book.my_book()
    app_mobile.simple_user_save_book.viewing_the_saved_section()
    app_mobile.simple_user_save_book.deleting_a_book_from_saved_ones()

    # ASSERT
    app_mobile.simple_user_save_book.checking_that_the_saved_section()
