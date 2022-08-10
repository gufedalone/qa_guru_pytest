import pytest
from selene.support.shared import browser


@pytest.fixture(scope='session', autouse=True)
def browser_window_size(request):
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]


@pytest.mark.parametrize("browser_window_size", [(1600, 900)], indirect=True)
def test_github_desktop():
    browser.open('https://github.com/')
    browser.element('a[href="/login"]').click()


@pytest.mark.parametrize("browser_window_size", [(750, 1334)], indirect=True)
def test_github_mobile():
    browser.open('https://github.com/')
    browser.element('svg.octicon-three-bars').click()
    browser.element('a[href="/login"]').click()
