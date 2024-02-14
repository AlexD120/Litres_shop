import allure
from selene import have, be
from selene.support.shared.jquery_style import s, ss
from appium.webdriver.common.appiumby import AppiumBy


class SimpleUserSaveBookPage:

    def __init__(self):

        self.add_to_favorite = s((AppiumBy.ID, 'ru.litres.android:id/bookPostpone'))
        self.go_to_the_section_my_book = ss(
            (AppiumBy.ID, 'ru.litres.android:id/navigation_bar_item_small_label_view')
        )
        self.skip_info = s(
            (AppiumBy.ID, 'ru.litres.android:id/btnMyBooksOnboardingClose')
        )
        self.section_the_saved = ss(
            (AppiumBy.ID, 'ru.litres.android:id/textViewBookSectionTitle')
        )
        self.should_name_book = s(
            (AppiumBy.ID, 'ru.litres.android:id/textViewBookName')
        )
        self.triple_dots_menu = s(
            (AppiumBy.ID, 'ru.litres.android:id/buttonTripleDots')
        )
        self.remove_book = ss((AppiumBy.CLASS_NAME, 'android.widget.TextView'))
        self.checking_section_saved = s(
            (AppiumBy.ID, 'ru.litres.android:id/textViewDescriptionEmptySection')
        )

    @allure.step("Adds the current book to the user's saved books")
    def add_to_favorites(self):
        self.add_to_favorite.should(be.visible).click()

    @allure.step("Navigates to the 'My Books' section")
    def my_book(self):
        self.go_to_the_section_my_book.element_by(have.text('My books')).click()
        self.skip_info.click()

    @allure.step("Verifies the title of the saved book")
    def viewing_the_saved_section(self):
        self.section_the_saved.element_by(have.text('Saved')).click()
        self.should_name_book.should(have.text('Головоломка'))

    @allure.step("Deletes a book from the user's saved books")
    def deleting_a_book_from_saved_ones(self):
        self.triple_dots_menu.click()
        self.remove_book.element_by(have.text('Remove from shelved')).click()

    @allure.step("Verifies that the saved section is empty")
    def checking_that_the_saved_section(self):
        self.checking_section_saved.should(
            have.text('Everything you save for later will be here.')
        )
