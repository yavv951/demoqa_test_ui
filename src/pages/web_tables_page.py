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

    """def check_have_text_on_fields(self, data: WebTablesPageModel):
        #Проверка, что текст иммется на странице, код был в первой версии тестов
        self.check_element_have_text_(WebTablesFormPageLocators.TABLES_FIELDS, data.first_name)
        self.check_element_have_text_(WebTablesFormPageLocators.TABLES_FIELDS, data.last_name)
        self.check_element_have_text_(WebTablesFormPageLocators.TABLES_FIELDS, data.user_email)
        self.check_element_have_text_(WebTablesFormPageLocators.TABLES_FIELDS, data.age)
        self.check_element_have_text_(WebTablesFormPageLocators.TABLES_FIELDS, data.salary)
        self.check_element_have_text_(WebTablesFormPageLocators.TABLES_FIELDS, data.department)"""

    def check_delete_element(self):
        self.check_element_have_text_by(index=1, locator=WebTablesFormPageLocators.EVEN_NUMBERS_LINE,
                                        text='')

    def check_elements_on_fourth_line(self, data: WebTablesPageModel):
        self.check_element_have_text_by(index=1, locator=WebTablesFormPageLocators.EVEN_NUMBERS_LINE,
                                        text=f"{data.first_name}\n{data.last_name}\n{data.age}\n{data.user_email}\n{data.salary}\n{data.department}")

    def check_elements_on_second_line(self, data: WebTablesPageModel):
        self.check_element_have_text_by(index=0, locator=WebTablesFormPageLocators.EVEN_NUMBERS_LINE,
                                        text=f"{data.first_name}\n{data.last_name}\n{data.age}\n{data.user_email}\n{data.salary}\n{data.department}")
