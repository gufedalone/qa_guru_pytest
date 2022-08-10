import time
import pytest
from selene.support.shared import browser


@pytest.fixture(params=[(1920, 1080), (1600, 900)],
                ids=["1920x1080", "1600x900"],
                scope='function'
                )
def stretched(request):
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]
    time.sleep(1)
    browser.open('https://github.com/')


@pytest.fixture(params=[(750, 1334), (828, 1792)],
                ids=["750x1334", "828x1792"],
                scope='function'
                )
def shrinked(request):
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]
    time.sleep(1)
    browser.open('https://github.com/')


def test_github_desktop(stretched):
    browser.element('a[href="/login"]').click()


def test_github_mobile(shrinked):
    browser.element('svg.octicon-three-bars').click()
    browser.element('a[href="/login"]').click()
