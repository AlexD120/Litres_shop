from litres_shop_test.page.ui.simple_should_user_registration_page import SimpleUserRegistrationPage
from litres_shop_test.page.ui.simple_should_catalog_page import SimpleShouldCatalogPage
from litres_shop_test.page.ui.simple_should_search_input_page import SimpleShouldSearchPage
from litres_shop_test.page.ui.simple_should_filter_page import SimpleShouldFilterPage
from litres_shop_test.page.ui.simple_should_book_description import SimpleShouldBookDescriptionPage
from litres_shop_test.page.ui.simple_should_favourites_page import SimpleShouldFavouritesPage
from litres_shop_test.page.ui.simple_should_cart_page import SimpleShouldCartPage
from litres_shop_test.page.mobile.simple_user_authorization_page import SimpleUserAuthorizationPage
from litres_shop_test.page.mobile.simple_search_book import SimpleUserSearchBookPage
from litres_shop_test.page.mobile.simple_authorization_and_addition_book_selected_page import SimpleUserSaveBookPage


class ApplicationUa:
    def __init__(self):
        self.simple_user_registration_page = SimpleUserRegistrationPage()
        self.simple_should_catalog_page = SimpleShouldCatalogPage()
        self.simple_should_search_page = SimpleShouldSearchPage()
        self.simple_should_filter_page = SimpleShouldFilterPage()
        self.simple_should_book_description = SimpleShouldBookDescriptionPage()
        self.simple_should_favourites_page = SimpleShouldFavouritesPage()
        self.simple_should_cart_page = SimpleShouldCartPage()


app = ApplicationUa()


class ApplicationMobile:
    def __init__(self):
        self.simple_user_authorization_page = SimpleUserAuthorizationPage()
        self.simple_search_book_page = SimpleUserSearchBookPage()
        self.simple_user_save_book = SimpleUserSaveBookPage()


app_mobile = ApplicationMobile()