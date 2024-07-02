from tests.conftest import screen_resolution
from selene import browser, be
import pytest


@pytest.mark.parametrize("screen_resolution", ["1920x1080", "540x960"], indirect=True)
def test_github(screen_resolution):
    browser.open("https://github.com")
    if screen_resolution == "1920x1080":
        browser.element(".HeaderMenu-link--sign-in").should(be.clickable).click()
    elif screen_resolution == "540x960":
        browser.element('[aria-label="Toggle navigation"].Button--link ').click()
        browser.element(".HeaderMenu-link--sign-in").should(be.clickable).click()