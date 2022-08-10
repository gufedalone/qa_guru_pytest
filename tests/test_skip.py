import time
import pytest
from selene.support.shared import browser


@pytest.fixture(params=[(1920, 1080), (1600, 900), (828, 1792), (750, 1334)],
                ids=["1920x1080", "1600x900", "828x1792", "750x1334"],
                scope='function'
                )
def browser_window_size(request):
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]
    time.sleep(1)
    browser.open('https://github.com/')


def test_github_desktop(browser_window_size):
    if (browser.config.window_width / browser.config.window_height) < 1:
        pytest.skip('Mobile resolution')
    browser.element('a[href="/login"]').click()


def test_github_mobile(browser_window_size):
    if (browser.config.window_width / browser.config.window_height) > 1:
        pytest.skip('Desktop resolution')
    browser.element('svg.octicon-three-bars').click()
    browser.element('a[href="/login"]').click()
