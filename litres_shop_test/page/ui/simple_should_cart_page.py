import allure
from selene import browser, have, be
from selene.support.shared.jquery_style import s


class SimpleShouldCartPage:
    def __init__(self):
        self.search_book_input = s('[data-testid="header__search-input--desktop"]')
        self.search_results_title = s('[data-testid="search-title__wrapper"]')
        self.checkbox_text = s('[id="art_types-text_book"]')
        self.selecting_book_from_search = s('[data-testid="art__title"]')
        self.book_title = s('h1[itemprop="name"]')
        self.book_add_button_to_cart = s(
            '[data-testid="book__addToCartButton--desktop"]'
        )
        self.book_go_to_cart_button = s('[data-testid="book__goToCartButton--desktop"]')
        self.cart_list_item = s('[data-testid="cart__listItem--12928406"]')
        self.cart_delete_button = s('[data-testid="cart__listDeleteButton--desktop"]')
        self.cart_modal_delete_button = s('[data-testid="cart_modalDeleteArt"]')
        self.cart_empty_state = s('[data-testid="cart__emptyState--wrapper"]')

    @allure.step('Open the main page')
    def open(self):
        browser.open('/')
        return self

    @allure.step('Search for a book')
    def search_book(self):
        self.search_book_input.type('Тилье головоломка').press_enter()

    @allure.step('Verify search results title')
    def verify_search_results_title(self):
        self.search_results_title.should(be.visible).should(
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

    @allure.step('Add the book to cart')
    def add_book_to_cart(self):
        self.book_add_button_to_cart.click()

    @allure.step('Navigate to the cart tab')
    def navigate_to_cart_tab(self):
        self.book_go_to_cart_button.double_click()

    @allure.step('Verify the book is in cart')
    def verify_book_in_cart(self):
        self.cart_list_item.should(have.text('Головоломка' and 'Франк Тилье' and '408'))

    @allure.step('Remove the book from cart')
    def remove_book_from_cart(self):
        self.cart_delete_button.click()
        self.cart_modal_delete_button.s('[type="button"]').should(
            have.exact_text('Удалить')
        ).click()

    @allure.step('Verify the book is removed from cart')
    def verify_book_removed_from_cart(self):
        self.cart_empty_state.should(be.visible).should(have.text('Корзина пуста'))
