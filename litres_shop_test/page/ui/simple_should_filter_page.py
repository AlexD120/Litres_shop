import allure
from selene import browser, have, be, by
from selene.support.shared.jquery_style import s


class SimpleShouldFilterPage:
    def __init__(self):
        self.new_book = s('[data-testid="lowerMenu_items"]').s(by.text("Популярное"))
        self.directory_sports = s(by.text('спорт, здоровье, красота'))
        self.check_directory_sports = s('[id="breadcrumbs"]')
        self.checkbox_text = s('[id="art_types-text_book"]')
        self.checkbox_languages_ru = s('[id="languages-ru"]')
        self.check_filter_title = s('.Genre-module__title__name_JuQ14')
        self.check_selection_checkboxes = s('.FiltersGrid-module__content_3Butd')

    @allure.step('Open main page')
    def open(self):
        browser.open('/')
        return self

    @allure.step('Opening the "NEW BOOK" section')
    def open_section_new_book(self):
        self.new_book.should(be.clickable).click()

    @allure.step('Selecting and checking directory "sports"')
    def open_directory_sport(self):
        self.directory_sports.double_click()
        self.check_directory_sports.should(have.text('спорт, здоровье, красота'))

    @allure.step('Selecting the text checkbox')
    def select_text_checkbox(self):
        self.checkbox_text.double_click()

    @allure.step('Selecting the Russian language checkbox')
    def select_russian_language_checkbox(self):
        self.checkbox_languages_ru.double_click()

    @allure.step('Checking filter header and selecting the appropriate checkboxes')
    def checking_title_and_selecting_checkboxes(self):
        self.check_filter_title.should(have.text('спорт, здоровье, красота'))
        self.check_selection_checkboxes.should(have.text('Текст' and 'Русский'))
