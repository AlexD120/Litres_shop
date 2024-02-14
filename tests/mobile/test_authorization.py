import allure
from litres_shop_test.helpers.application import app_mobile
from litres_shop_test.helpers.skip_onboarding import skip_onboarding_question


@allure.title("User authorization test")
@allure.feature("Authorization")
@allure.story("Successful user login")
@allure.label("UI")
@allure.tag("smoke")
@allure.severity("critical")
@allure.label("owner", "Davydov")
def test_users_authorization():
    #ARRANGE
    skip_onboarding_question()

    #ACT
    app_mobile.simple_user_authorization_page.account()
    app_mobile.simple_user_authorization_page.authorization_account()
    app_mobile.simple_user_authorization_page.skip_number_notifications()
    app_mobile.simple_user_authorization_page.about_the_users_account()

    #ASSERT
    app_mobile.simple_user_authorization_page.should_login_name()
