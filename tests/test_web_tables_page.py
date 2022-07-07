from src.models.web_tables_page import WebTablesPageModel


class TestWebTablesPage:
    """
    Тест сьют. Тестирование странцы web tables
    """

    def test_web_tables(self, app_web_tables_page):
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
        app_web_tables_page.web_tables_page\
            .click_add_button()\
            .fill_form_registration(field_first)\
            .click_submit_button()\
            .check_elements_on_fourth_line(field_first)
        field_second = WebTablesPageModel.random()
        app_web_tables_page.web_tables_page\
            .click_edit_form()\
            .fill_form_registration(field_second).click_submit_button()\
            .check_elements_on_second_line(field_second)\
            .delete_record()\
            .check_delete_element()

