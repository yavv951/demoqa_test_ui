
from src.pages.automation_practice_form import AutomationPracticeFormPage
from src.pages.base_page import BasePage
from src.pages.web_tables_page import WebTablesPage


class Application:
    def __init__(self, base_url):
        self.url = base_url
        self.practice_form_page = AutomationPracticeFormPage(self)
        self.web_tables_page = WebTablesPage(self)

    @staticmethod
    def close():
        BasePage.close()

