import time
import pytest
from selene.support.shared import browser

desktop = pytest.mark.parametrize("browser_window_size",
                                  [(1920, 1080), (1600, 900)],
                                  ids=["1920x1080", "1600x900"],
                                  indirect=True
                                  )

mobile = pytest.mark.parametrize("browser_window_size",
                                 [(828, 1792), (750, 1334)],
                                 ids=["828x1792", "750x1334"],
                                 indirect=True
                                 )


@pytest.fixture(params=[(1920, 1080), (1600, 900), (828, 1792), (750, 1334)],
                scope='function'
                )
def browser_window_size(request):
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]
    time.sleep(1)
    browser.open('https://github.com/')


@desktop
def test_github_desktop(browser_window_size):
    browser.element('a[href="/login"]').click()


@mobile
def test_github_mobile(browser_window_size):
    browser.element('svg.octicon-three-bars').click()
    browser.element('a[href="/login"]').click()
