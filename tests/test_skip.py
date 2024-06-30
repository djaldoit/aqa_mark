import pytest
from selene import browser, be
from conftest import setup_screen_resolution


@pytest.mark.parametrize("setup_screen_resolution", ["1920x1080", "540x960"], indirect=True)
def test_github_desktop(setup_screen_resolution):
    if setup_screen_resolution == "mobile":
        pytest.skip(reason="Пропускаем тест для 540x960")
    else:
        browser.open("https://github.com")
        browser.element(".HeaderMenu-link--sign-in").should(be.clickable).click()


@pytest.mark.parametrize("setup_screen_resolution", ["1920x1080", "540x960"], indirect=True)
def test_github_mobile(setup_screen_resolution):
    if setup_screen_resolution == "desktop":
        pytest.skip(reason="Пропускаем тест для 1920x1080")
    else:
        browser.open("https://github.com")
        browser.element('[aria-label="Toggle navigation"].Button--link ').click()
        browser.element(".HeaderMenu-link--sign-in").should(be.clickable).click()