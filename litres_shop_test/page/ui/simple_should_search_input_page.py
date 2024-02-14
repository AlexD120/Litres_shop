from selene import browser, have, be
from selene.support.shared.jquery_style import s
import allure


class SimpleShouldSearchPage:
    def __init__(self):
        self.search_book = s('[data-testid="header__search-input--desktop"]')
        self.checking_search_result = s('[data-testid="search-title__wrapper"]')
        self.button_clear = s('[data-testid="header__search-form--desktop"]')

    @allure.step('Open main page')
    def open(self):
        browser.open('/')
        return self

    @allure.step('2. Enter the title of the book "Слово пацана" in the search field')
    def search_book_one(self):
        self.search_book.should(be.blank).type('Слово пацана').press_enter()

    @allure.step('Check the search result book "Слово пацана"')
    def should_search_book_one(self):
        self.checking_search_result.should(
            have.exact_text('Результаты поиска «Слово пацана»')
        )
        self.button_clear.s('svg[fill="none"]').double_click()

    @allure.step('Enter the title of the book "Шантарам" in the search field')
    def search_book_two(self):
        self.search_book.type('Шантарам').press_enter()

    @allure.step('Check the search result book "Шантарам"')
    def should_search_book_two(self):
        self.checking_search_result.should(be.visible).should(
            have.exact_text('Результаты поиска «Шантарам»')
        )
