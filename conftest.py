import pytest
from selene import browser


@pytest.fixture(params=["1920x1080"])
def desktop_screen_resolution(request):
    width, height = map(int, request.param.split("x"))
    browser.config.window_width = width
    browser.config.window_height = height

    yield

    browser.quit()


@pytest.fixture(params=["540x960"])
def mobile_screen_resolution(request):
    width, height = map(int, request.param.split("x"))
    browser.config.window_width = width
    browser.config.window_height = height

    yield

    browser.quit()


@pytest.fixture(params=["1920x1080", "540x960"])
def screen_resolution(request):
    width, height = map(int, request.param.split("x"))
    browser.config.window_width = width
    browser.config.window_height = height

    yield

    browser.quit()


@pytest.fixture(params=["1920x1080", "540x960"])
def setup_screen_resolution(request):
    width, height = map(int, request.param.split("x"))
    browser.config.window_width = width
    browser.config.window_height = height
    if request.param in ["1920x1080"]:
        yield "desktop"
    else:
        yield "mobile"

    browser.quit()