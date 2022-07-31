import pytest
from selene.support.shared import browser
from src.pages.application import Application


@pytest.fixture
def app(request):
    base_url = request.config.getoption("--base-url")
    browser.open_url(base_url).driver.set_window_size(width=1980, height=1280)
    app = Application(base_url)
    yield app
    app.close()

@pytest.fixture
def app_web_tables_page(request):
    base_url = request.config.getoption("--web-tables-url")
    browser.open_url(base_url).driver.set_window_size(width=1980, height=1280)
    app = Application(base_url)
    yield app
    app.close()

def pytest_addoption(parser):
    parser.addoption(
        "--base-url",
        action="store",
        default="https://demoqa.com/automation-practice-form",
        help="enter base_url"
    )

    parser.addoption(
        "--web-tables-url",
        action="store",
        default="https://demoqa.com/webtables",
        help="enter base_url"
    )