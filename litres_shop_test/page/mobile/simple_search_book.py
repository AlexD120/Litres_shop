import allure
from selene import have
from selene.support.shared.jquery_style import s, ss
from appium.webdriver.common.appiumby import AppiumBy


class SimpleUserSearchBookPage:

    def __init__(self):
        self.search_site_bar = ss(
            (AppiumBy.ID, 'ru.litres.android:id/navigation_bar_item_small_label_view')
        ).element_by(have.text('Search'))
        self.search_query = s((AppiumBy.ID, 'ru.litres.android:id/et_search_query'))
        self.selecting_search_value = s(
            (AppiumBy.ID, 'ru.litres.android:id/textViewItemSearchSuggestText')
        )
        self.choose_book_search_option = s(
            (AppiumBy.XPATH, '//android.widget.TextView[@text="BOOKS"]')
        )
        self.select_first_result_from_search_list = ss(
            (AppiumBy.ID, 'ru.litres.android:id/textViewBookName')
        )
        self.book_title = s((AppiumBy.ID, 'ru.litres.android:id/tvBookTitle'))

    @allure.step("Search for a book")
    def search(self):
        self.search_site_bar.click()
        self.search_query.type(text='Франк Тилье Головоломка')
        self.selecting_search_value.click()
        self.choose_book_search_option.click()
        self.select_first_result_from_search_list.first.click()

    @allure.step("Verify book title")
    def verify_book_title(self):
        self.book_title.should(have.text('Головоломка'))
