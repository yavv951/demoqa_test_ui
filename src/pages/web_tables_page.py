import time
from src.locators.automation_practice_form_locators import PracticeFormPageLocators
from src.locators.web_tables_locators import WebTablesFormPageLocators
from src.models.constants import Constants
from src.models.web_tables_page import WebTablesPageModel
from src.pages.base_page import BasePage, SelectList


class WebTablesPage(BasePage):
    """
     Страница таблиц
    """

    def fill_form_registration(self, data: WebTablesPageModel):
        """Ввод данных в форму регистрации"""
        self.fill_element(WebTablesFormPageLocators.FIRSTNAME, data.first_name)
        self.fill_element(WebTablesFormPageLocators.LASTNAME, data.last_name)
        self.fill_element(WebTablesFormPageLocators.USER_EMAIL, data.user_email)
        self.fill_element(WebTablesFormPageLocators.AGE, data.age)
        self.fill_element(WebTablesFormPageLocators.SALARY, data.salary)
        self.fill_element(WebTablesFormPageLocators.DEPARTAMENT, data.department)

    def click_add_button(self):
        self.click_element(WebTablesFormPageLocators.BUTTON_ADD)

    def click_submit_button(self):
        self.click_element(WebTablesFormPageLocators.SUBMIT)

    def click_edit_form(self):
        self.click_element(WebTablesFormPageLocators.EDIT_BUTTON)

    def delete_record(self):
        self.click_element(WebTablesFormPageLocators.DELETE_RECORD)

    def check_have_text_on_fields(self, data: WebTablesPageModel):
        """"Проверка, что текст иммется на странице"""
        self.check_element_have_text_(WebTablesFormPageLocators.SECOND_FIELD, data.first_name)
        self.check_element_have_text_(WebTablesFormPageLocators.SECOND_FIELD, data.last_name)
        self.check_element_have_text_(WebTablesFormPageLocators.SECOND_FIELD, data.age)
        self.check_element_have_text_(WebTablesFormPageLocators.SECOND_FIELD, data.salary)
        self.check_element_have_text_(WebTablesFormPageLocators.SECOND_FIELD, data.department)
