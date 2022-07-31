import pytest
from selene.support.shared import browser

from src.pages.application import Application
import os

from selenium import webdriver
from dotenv import load_dotenv

from utils import attach

DEFAULT_BROWSER_VERSION = "100.0"


def pytest_addoption(parser):
    parser.addoption(
        '--browser_version',
        default='100.0'
    )
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


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='function', autouse=True)
def setup_browser(request):
    browser_version = request.config.getoption('--browser_version')
    browser_version = browser_version if browser_version != "" else DEFAULT_BROWSER_VERSION
    #options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": browser_version,
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    #options.capabilities.update(selenoid_capabilities)
    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')
    browser.config.driver = webdriver.Remote(
        command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub",
        desired_capabilities=selenoid_capabilities
    )
    yield setup_browser


@pytest.fixture
def app(request, setup_browser):
    base_url = request.config.getoption("--base-url")
    browser.open_url(base_url).driver.set_window_size(width=1980, height=1280)
    app = Application(base_url)
    yield app
    app.close()


@pytest.fixture
def app_web_tables_page(request, setup_browser):
    #browser = setup_browser
    base_url = request.config.getoption("--web-tables-url")
    browser.open_url(base_url).driver.set_window_size(width=1980, height=1280)
    app = Application(base_url)
    yield app
    app.close()
