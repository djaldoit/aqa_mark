from selene import browser, be
from tests.conftest import setup_screen_resolution


def test_github_desktop(setup_screen_resolution):
    if setup_screen_resolution == "desktop":
        browser.open("https://github.com")
        browser.element(".HeaderMenu-link--sign-in").should(be.clickable).click()
    elif setup_screen_resolution == "mobile":
        browser.open("https://github.com")
        browser.element('[aria-label="Toggle navigation"].Button--link ').click()
        browser.element(".HeaderMenu-link--sign-in").should(be.clickable).click()
