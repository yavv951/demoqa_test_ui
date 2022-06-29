import pytest
from src.pages.application import Application
from src.pages.base_page import BasePage

@pytest.fixture
def open_browser(request):
    base_url = request.config.getoption("--base-url")
    BasePage.open_page(base_url)
    app = Application(base_url)
    yield app
    app.close()

@pytest.fixture
def open_browser_web_tables_page(request):
    base_url = request.config.getoption("--web-tables-url")
    BasePage.open_page(base_url)
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