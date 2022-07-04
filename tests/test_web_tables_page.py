import time

from src.models.web_tables_page import WebTablesPageModel


class TestWebTablesPage:
    """
    Тест сьют. Тестирование странцы web tables
    """

    def test_web_tables(self, open_browser_web_tables_page):
        """
        Тест кейс 0002
        1. открыть страницу https://demoqa.com/webtables
        2. Нажать на кнопку добавить(Add)
        3. Заполнить форму регистрации:
           First Name
           Last Name
           Email
           Age
           Salary
           Department
        4. Проверить,что заполненные поля отобразились в форме регистрациию
        5. Редактируем  все поля во второй строке
        6. Проверяем, что поля отредактированы
        7. Удаляем третью строку
        8. Проверяем,что строка удалилась
        """
        field_first = WebTablesPageModel.random()
        open_browser_web_tables_page.web_tables_page.click_add_button()
        open_browser_web_tables_page.web_tables_page.fill_form_registration(field_first)
        open_browser_web_tables_page.web_tables_page.click_submit_button()
        open_browser_web_tables_page.web_tables_page.check_elements_on_fourth_line(field_first)
        field_second = WebTablesPageModel.random()
        open_browser_web_tables_page.web_tables_page.click_edit_form()
        open_browser_web_tables_page.web_tables_page.fill_form_registration(field_second)
        open_browser_web_tables_page.web_tables_page.click_submit_button()
        open_browser_web_tables_page.web_tables_page.check_elements_on_second_line(field_second)
        open_browser_web_tables_page.web_tables_page.delete_record()
        open_browser_web_tables_page.web_tables_page.check_delete_element()





