from litres_shop_test.helpers.application import app
import allure


@allure.title('Successful user login')
@allure.feature('User authentication')
@allure.story('Registered users can log in successfully')
@allure.label('UI')
@allure.tag('smoke')
@allure.severity('critical')
@allure.label("owner", "Davydov")
def test_registration_user(browser_config):
    #ARRANGE
    app.simple_user_registration_page.open()
    app.simple_user_registration_page.navigate_to_login_tab()

    #ACT
    app.simple_user_registration_page.enter_login_credentials()
    app.simple_user_registration_page.skip_phone_number()
    app.simple_user_registration_page.login_users_profile()

    #ASSERT
    app.simple_user_registration_page.should_profile()
