import pytest
from selene.support.shared import browser


@pytest.fixture(scope='function', autouse=True)
def browser_window_size(request):
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]
    browser.open('https://github.com/')


@pytest.mark.parametrize("browser_window_size", [(1600, 900), (828, 1792)], indirect=True)
def test_github_desktop():
    try:
        browser.element('a[href="/login"]').click()
    except AssertionError:
        pytest.xfail(reason="Mobile resolution")


@pytest.mark.parametrize("browser_window_size", [(750, 1334), (1920, 1080)], indirect=True)
def test_github_mobile():
    try:
        browser.element('svg.octicon-three-bars').click()
        browser.element('a[href="/login"]').click()
    except AssertionError:
        pytest.xfail(reason="Desktop resolution")
