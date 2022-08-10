import pytest
from selene.support.shared import browser


@pytest.fixture(params=[(1920, 1080), (1600, 900)], scope='function')
def stretched(request):
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]
    browser.open('https://github.com/')


@pytest.fixture(params=[(750, 1334), (1920, 1080)], scope='function')
def shrinked(request):
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]
    browser.open('https://github.com/')


def test_github_desktop(stretched):
    try:
        browser.element('a[href="/login"]').click()
    except AssertionError:
        pytest.xfail(reason="Mobile resolution")


def test_github_mobile(shrinked):
    try:
        browser.element('svg.octicon-three-bars').click()
        browser.element('a[href="/login"]').click()
    except AssertionError:
        pytest.xfail(reason="Desktop resolution")
