import pytest
from selene.support.shared import browser


@pytest.fixture(params=[(1920, 1080), (1600, 900), (828, 1792), (750, 1334)], scope='session', autouse=True)
def browser_window_size(request):
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]


def test_github_desktop(browser_window_size):
    browser.open('https://github.com/')
    if browser.config.window_width < 1012:
        pytest.skip('Mobile resolution')
    browser.element('a[href="/login"]').click()


def test_github_mobile(browser_window_size):
    browser.open('https://github.com/')
    if browser.config.window_width > 1011:
        pytest.skip('Desktop resolution')
    browser.element('svg.octicon-three-bars').click()
    browser.element('a[href="/login"]').click()
