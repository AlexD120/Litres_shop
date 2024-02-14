import os
import allure
from dotenv import load_dotenv
from selene import have, be
from selene.support.shared.jquery_style import s
from appium.webdriver.common.appiumby import AppiumBy


class SimpleUserAuthorizationPage:
    load_dotenv()
    login = os.getenv('LOGIN_USER')
    password = os.getenv('PASSWORD_USER')

    def __init__(self):
        self.login_site_bar = s((AppiumBy.ACCESSIBILITY_ID, 'Log in'))
        self.login_button = s((AppiumBy.ID, 'ru.litres.android:id/login_button'))
        self.enter_login = s((AppiumBy.ID, 'ru.litres.android:id/loginEditText'))
        self.continue_button = s((AppiumBy.ID, 'ru.litres.android:id/continueButton'))
        self.enter_password = s((AppiumBy.ID, 'ru.litres.android:id/passwordEditText'))
        self.skip_number = s((AppiumBy.ID, 'ru.litres.android:id/laterButton'))
        self.user_login = s((AppiumBy.ID, 'ru.litres.android:id/user_login'))
        self.verify_login_name = s(
            (AppiumBy.ID, 'ru.litres.android:id/navigation_bar_item_large_label_view')
        )

    @allure.step("Open account menu")
    def account(self):
        self.login_site_bar.click()

    @allure.step("Start authorization process")
    def authorization_account(self):
        self.login_button.click()
        self.enter_login.type(self.login)
        self.continue_button.click()
        self.enter_password.type(self.password)
        self.continue_button.click()

    @allure.step("Skip phone number verification (if present)")
    def skip_number_notifications(self):
        self.skip_number.should(be.visible).click()

    @allure.step("Verify user login is displayed")
    def about_the_users_account(self):
        self.user_login.should(have.text(self.login))

    @allure.step("Verify username is displayed on main screen")
    def should_login_name(self):
        self.verify_login_name.should(have.text(self.login))
