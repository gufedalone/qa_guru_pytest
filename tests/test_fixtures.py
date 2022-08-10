import pytest
from selene.support.shared import browser


@pytest.fixture(scope='function')
def stretched():
    browser.config.window_width = 1600
    browser.config.window_height = 900


@pytest.fixture(scope='function')
def shrinked():
    browser.config.window_width = 828
    browser.config.window_height = 1792


def test_github_desktop(stretched):
    browser.open('https://github.com/')
    browser.element('a[href="/login"]').click()


def test_github_mobile(shrinked):
    browser.open('https://github.com/')
    browser.element('svg.octicon-three-bars').click()
    browser.element('a[href="/login"]').click()
