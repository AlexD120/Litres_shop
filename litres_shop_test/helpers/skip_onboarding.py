import allure
from selene.support.shared.jquery_style import s, ss
from appium.webdriver.common.appiumby import AppiumBy
from selene import be, have


@allure.step('Skip send notifications')
def skip_onboarding_question():
    if s((AppiumBy.ID, "ru.litres.android:id/choosebutton")).matching(be.clickable):
        s((AppiumBy.ID, "ru.litres.android:id/choosebutton")).click()


    if (
        ss((AppiumBy.CLASS_NAME, 'android.widget.Button'))
        .element_by(have.text('Don’t allow'))
        .matching(be.clickable)
    ):
        ss((AppiumBy.CLASS_NAME, 'android.widget.Button')).element_by(
            have.text('Don’t allow')
        ).click()

    if s(
        (AppiumBy.ID, "ru.litres.android:id/navigation_bar_item_large_label_view")
    ).matching(be.clickable):
        s(
            (
                AppiumBy.ID,
                "ru.litres.android:id/navigation_bar_item_large_label_view",
            )
        ).press("ESCAPE")


    s((AppiumBy.ID, 'ru.litres.android:id/btnDisableAdultContent')).with_(timeout=15).should(be.visible).click()


    s((AppiumBy.ID, 'ru.litres.android:id/btnConfirmDialogCancel')).click()

    if s((AppiumBy.CLASS_NAME, 'android.widget.Button')).matching(be.clickable):
        s((AppiumBy.CLASS_NAME, 'android.widget.Button')).click()
