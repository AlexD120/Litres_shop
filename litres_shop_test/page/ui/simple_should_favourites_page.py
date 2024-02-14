import allure
from selene import browser, have, be, by
from selene.support.shared.jquery_style import s


class SimpleShouldFavouritesPage:
    def __init__(self):
        self.search_book_input = s('[data-testid="header__search-input--desktop"]')
        self.search_results_title = s('[data-testid="search-title__wrapper"]')
        self.checkbox_text = s('[id="art_types-text_book"]')
        self.selecting_book_from_search = s('[data-testid="art__title"]')
        self.book_title = s('h1[itemprop="name"]')
        self.select_favorites = s(by.text('Отложить'))
        self.moving_deferred = s('[data-testid="tab-favorite"]')
        self.checking_deferred_book = s('#liked-arts')
        self.checking_price_book = s('.simple-price')
        self.open_dropdown = s(
            '[data-testid="popover__baseElement"] a[class*=contextMenu__button]'
        )
        self.delete_from_deferred = s(by.text('Убрать из отложенного'))
        self.checking_book_deleted_deferred = s('#liked-arts')

    @allure.step('Open the main page')
    def open(self):
        browser.open('/')
        return self

    @allure.step('Search for a book')
    def search_book(self):
        self.search_book_input.type('Тилье головоломка').press_enter()

    @allure.step('Verify search results title')
    def verify_search_results_title(self):
        self.search_results_title.should(
            have.exact_text('Результаты поиска «Тилье головоломка»')
        )

    @allure.step('Selecting the text checkbox')
    def select_text_checkbox(self):
        self.checkbox_text.double_click()

    @allure.step('Open the book from search results')
    def open_book_from_search_results(self):
        self.selecting_book_from_search.should(be.clickable).should(
            have.text('Головоломка')
        ).click()

    @allure.step('Verify book title')
    def verify_book_title(self):
        self.book_title.should(have.text('Головоломка'))

    @allure.step('Add the book to favorites')
    def add_book_to_favorites(self):
        self.select_favorites.should(be.clickable).click()

    @allure.step('Navigate to the favorites tab')
    def navigate_to_favorites_tab(self):
        self.moving_deferred.should(have.text('1')).click()

    @allure.step('Verify the book is in favorites')
    def verify_book_in_favorites(self):
        self.checking_deferred_book.should(have.text('Франк Тилье' and 'Головоломка'))
        self.checking_price_book.should(have.text('408'))

    @allure.step('Open the dropdown list')
    def open_dropdown_list(self):
        self.open_dropdown.hover().click()

    @allure.step('Remove the book from favorites')
    def remove_book_from_favorites(self):
        self.delete_from_deferred.should(have.text('Убрать из отложенного')).should(
            be.visible
        ).click()

    @allure.step('Verify the book is removed from favorites')
    def verify_book_removed_from_favorites(self):
        self.checking_book_deleted_deferred.should(
            have.no.text('Франк Тилье' and 'Головоломка')
        )
