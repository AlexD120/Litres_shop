import allure
from selene import browser, have, by
from selene.support.shared.jquery_style import s


class SimpleShouldCatalogPage:
    def __init__(self):
        self.enter_catalog = s('[data-testid="header-catalog-button"]')
        self.choosing_catalog_hobby = s(by.text('Хобби, досуг'))
        self.choosing_catalog_skills = s(by.text('Знания и навыки'))
        self.choosing_catalog_serious_reading = s(by.text('Серьезное чтение'))
        self.checking_directory_header = s('.Genre-module__title_MILPj')
        self.checking_catalog_section = s('[data-testid="breadcrumbs__wrapper"]')

    @allure.step('Open main page')
    def open(self):
        browser.open('/')
        return self

    @allure.step('Open catalog "hobby" ')
    def open_catalog_hobby(self):
        self.enter_catalog.click()
        self.choosing_catalog_hobby.click()

    @allure.step('Check directory section "hobby" ')
    def should_directory_section_hobby(self):
        self.checking_directory_header.should(have.exact_text('хобби, досуг'))
        self.checking_catalog_section.should(have.text('хобби, досуг'))

    @allure.step('Open catalog "skills" ')
    def open_catalog_skills(self):
        self.enter_catalog.click()
        self.choosing_catalog_skills.click()

    @allure.step('Check directory section "skills" ')
    def should_directory_section_skills(self):
        self.checking_directory_header.should(have.exact_text('знания и навыки'))
        self.checking_catalog_section.should(have.text('знания и навыки'))

    @allure.step('Open catalog "serious_reading" ')
    def open_catalog_serious_reading(self):
        self.enter_catalog.click()
        self.choosing_catalog_serious_reading.click()

    @allure.step('Check directory section "serious_reading" ')
    def should_directory_section_serious_reading(self):
        self.checking_directory_header.should(have.exact_text('серьезное чтение'))
        self.checking_catalog_section.should(have.text('серьезное чтение'))
