from src.locators.automation_practice_form_locators import PracticeFormPageLocators
from src.models.constants import Constants
from src.models.automation_practice_form import PracticeFormPageModel
from src.pages.base_page import BasePage, SelectList


class AutomationPracticeFormPage(BasePage):
    """
    Страница Practice Form
    """

    def input_information_student(self, data: PracticeFormPageModel):
        """Ввод данных в форму регистрации"""
        self.fill_element(PracticeFormPageLocators.FIRSTNAME, data.first_name)
        self.fill_element(PracticeFormPageLocators.LASTNAME, data.last_name)
        self.fill_element(PracticeFormPageLocators.USEREMAIL, data.user_email)
        self.fill_element(PracticeFormPageLocators.USERNUMBER, data.user_number)
        self.fill_element_and_press_enter(PracticeFormPageLocators.SUBJECTBLANK, data.subjects)
        self.fill_element(PracticeFormPageLocators.CURRENTADDRESS, data.current_address)

    def input_gender(self, data: PracticeFormPageModel):
        self.click_radio_button(PracticeFormPageLocators.GENDER, data.gender)

    def input_hobbies(self, data: PracticeFormPageModel):
        self.click_radio_button(PracticeFormPageLocators.HOBBIES, data.hobbies)

    def click_submit(self):
        self.click_element(PracticeFormPageLocators.SUBMIT)

    def fill_state_and_city(self, data: PracticeFormPageModel):
        self.fill_element_and_press_enter(PracticeFormPageLocators.STATE, data.state)
        self.fill_element_and_press_enter(PracticeFormPageLocators.CITY, data.city)

    def check_have_text_on_submiting_form(self, data: PracticeFormPageModel):
        """"Проверка, что текст иммется на странице"""
        self.check_element_have_text(PracticeFormPageLocators.MODAL_TITLE, Constants.TEXT)
        self.check_element_have_text(PracticeFormPageLocators.MODAL_FORM_STUDENT_INFO, 'Ivan Ivanov')
        self.check_element_have_text(PracticeFormPageLocators.MODAL_FORM_STUDENT_INFO, data.user_email)
        self.check_element_have_text(PracticeFormPageLocators.MODAL_FORM_STUDENT_INFO, data.gender)
        self.check_element_have_text(PracticeFormPageLocators.MODAL_FORM_STUDENT_INFO, data.user_number)
        self.check_element_have_text(PracticeFormPageLocators.MODAL_FORM_STUDENT_INFO,
                                     f"{'15'} {'February'},{data.year}")
        self.check_element_have_text(PracticeFormPageLocators.MODAL_FORM_STUDENT_INFO, data.subjects)
        self.check_element_have_text(PracticeFormPageLocators.MODAL_FORM_STUDENT_INFO, data.hobbies)
        self.check_element_have_text(PracticeFormPageLocators.MODAL_FORM_STUDENT_INFO, 'my_photo.jpg')
        self.check_element_have_text(PracticeFormPageLocators.MODAL_FORM_STUDENT_INFO, data.current_address)
        self.check_element_have_text(PracticeFormPageLocators.MODAL_FORM_STUDENT_INFO, f"{'Haryana'} {data.city}"),

    def choose_image_file(self, image_file):
        self.load_file(PracticeFormPageLocators.UPLOADPICTURE, image_file)

    def fill_date_form(self, data: PracticeFormPageModel):
        self.click_element(PracticeFormPageLocators.DATE_FORM)
        element_month = self.find_element(PracticeFormPageLocators.MONTH)
        element_year = self.find_element(PracticeFormPageLocators.YEAR)
        SelectList(element_month).select_by_value(data.month)
        SelectList(element_year).select_by_value(data.year)
        self.click_element(PracticeFormPageLocators.DAY)
