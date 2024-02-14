import allure
from selene import browser, have, be
from selene.support.shared.jquery_style import s


class SimpleShouldBookDescriptionPage:
    def __init__(self):
        self.search_book_input = s('[data-testid="header__search-input--desktop"]')
        self.search_results_title = s('[data-testid="search-title__wrapper"]')
        self.checkbox_text = s('[id="art_types-text_book"]')
        self.selecting_book_from_search = s('[data-testid="art__title"]')
        self.book_title = s('h1[itemprop="name"]')
        self.author_name = s('[data-testid="book-author__avatarName"]')
        self.book_description = s('[data-testid="book-description__wrapper"]')

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
        self.checkbox_text.hover().double_click()

    @allure.step('Open the book from search results')
    def open_book_from_search_results(self):
        self.selecting_book_from_search.should(be.clickable).should(
            have.text('Головоломка')
        ).click()

    @allure.step('Verify book title')
    def verify_book_title(self):
        self.book_title.should(have.text('Головоломка'))

    @allure.step('Verify author name')
    def verify_author_name(self):
        self.author_name.should(have.text('Франк Тилье'))

    @allure.step('Verify book description')
    def verify_book_description(self):
        self.book_description.hover().should(
            have.text('В новом триллере Франка Тилье «Головоломка»')
        )
