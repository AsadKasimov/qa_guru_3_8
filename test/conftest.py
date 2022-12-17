import pytest

from selene.support.shared import browser


@pytest.fixture()
def set_window_size():
    browser.config.window_width = 920
    browser.config.window_width = 300


@pytest.fixture()
def open_(set_window_size):
    browser.config.base_url = 'https://demoqa.com'

    yield

    browser.quit()


