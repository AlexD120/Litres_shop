import os
import allure
from selene import browser, have, be, by
from selene.support.shared.jquery_style import s
from dotenv import load_dotenv


class SimpleUserRegistrationPage:
    load_dotenv()
    login_user = os.getenv('LOGIN_USER')
    login_password = os.getenv('PASSWORD_USER')

    def __init__(self):
        self.enter_user = s('[data-testid="tab-login"]')
        self.login = s('[name="email"')
        self.password = s('[name="pwd"')
        self.add_phone_number = s(by.text('Позже'))
        self.profile = s('[data-testid="header__profile-button"]')
        self.should_users_profile = s('#react-lc')

    @allure.step('Open main page')
    def open(self):
        browser.open('/')
        return self

    @allure.step('Navigate to login tab')
    def navigate_to_login_tab(self):
        self.enter_user.click()

    @allure.step('Enter login credentials')
    def enter_login_credentials(self):
        self.login.click().type(self.login_user).press_enter()
        self.password.click().type(self.login_password).press_enter()

    @allure.step('Skip phone number prompt')
    def skip_phone_number(self):
        self.add_phone_number.should(be.visible).click()

    @allure.step('Open user profile')
    def login_users_profile(self):
        self.profile.click()

    @allure.step('Verify profile name')
    def should_profile(self):
        self.should_users_profile.should(have.text('davydov'))
