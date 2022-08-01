import allure
from allure_commons.types import Severity
from selene.support.shared import browser

from src.models.web_tables_page import WebTablesPageModel
from utils import attach


class TestWebTablesPage:
    """
    Тест сьют. Тестирование странцы web tables
    """

    @allure.tag('WEB UI')
    @allure.severity(Severity.CRITICAL)
    @allure.label('Owner', 'Vadim')
    @allure.feature('Testing site qa guru with selene')
    @allure.story(f'Тест кейс 0002 Форма регистрации студента')
    @allure.link('https://github.com/yavv951', name='Owner')
    def test_web_tables(self, app_web_tables_page):
        field_first = WebTablesPageModel.random()
        app_web_tables_page.web_tables_page \
            .click_add_button() \
            .fill_form_registration(field_first) \
            .click_submit_button() \
            .check_elements_on_fourth_line(field_first)
        field_second = WebTablesPageModel.random()
        app_web_tables_page.web_tables_page \
            .click_edit_form() \
            .fill_form_registration(field_second) \
            .click_submit_button() \
            .check_elements_on_second_line(field_second) \
            .delete_record() \
            .check_delete_element()

        attach.add_html(browser)
        attach.add_screenshot(browser)
        attach.add_logs(browser)
        attach.add_video(browser)
