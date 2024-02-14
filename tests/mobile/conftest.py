import os
import allure
import allure_commons
import pytest
from appium import webdriver
from dotenv import load_dotenv
from selene import browser, support
from litres_shop_test.utils import allure_attach


def pytest_addoption(parser):
    parser.addoption(
        "--context",
        required=False,
        default="bstack",
        choices=['local_emulator', 'bstack'],
    )


def pytest_configure(config):
    context = config.getoption("--context")
    load_dotenv(dotenv_path=f'.env.{context}')


@pytest.fixture
def context(request):
    return request.config.getoption("--context")


@pytest.fixture(scope='function', autouse=True)
def android_mobile_management(context):
    from config import config

    options = config.to_driver_options(context=context)

    with allure.step('setup app session'):
        browser.config.driver = webdriver.Remote(
            options.get_capability('remote_url'), options=options
        )

    browser.config.timeout = float(os.getenv('timeout', 15))

    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext
    )

    yield

    allure_attach.screenshot()

    allure_attach.page_source_xml()

    session_id = browser.driver.session_id

    with allure.step('tear down app session with id'):
        browser.quit()

    if context == 'bstack':
        allure_attach.bstack_video(session_id)
