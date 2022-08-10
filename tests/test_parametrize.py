import time
import pytest
from selene.support.shared import browser


resolution = pytest.mark.parametrize("browser_window_size",
                                     [(1920, 1080), (1600, 900), (828, 1792), (750, 1334)],
                                     ids=["1920x1080", "1600x900", "828x1792", "750x1334"],
                                     indirect=True
                                     )


@pytest.fixture(scope='function', autouse=True)
def browser_window_size(request):
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]
    time.sleep(1)
    browser.open('https://github.com/')


@resolution
def test_github_desktop():
    try:
        browser.element('a[href="/login"]').click()
    except AssertionError:
        pytest.xfail(reason="Mobile resolution")


@resolution
def test_github_mobile():
    try:
        browser.element('svg.octicon-three-bars').click()
        browser.element('a[href="/login"]').click()
    except AssertionError:
        pytest.xfail(reason="Desktop resolution")
