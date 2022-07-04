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
        """ Метод ввода через написание значений state и city и нажатия на enter"""
        self.fill_element_and_press_enter(PracticeFormPageLocators.STATE, data.state)
        self.fill_element_and_press_enter(PracticeFormPageLocators.CITY, data.city)

    def input_state_city(self, data: PracticeFormPageModel):
        """Метод ввода значений state и city через выбор из выпадающего списка"""
        self.select(locator=PracticeFormPageLocators.STATE, locator_2=PracticeFormPageLocators.STATE_CITY_OPTION,
                    option=data.state)
        self.select(locator=PracticeFormPageLocators.CITY, locator_2=PracticeFormPageLocators.STATE_CITY_OPTION,
                    option=data.city)


    def check_have_text_on_submiting_form(self, data: PracticeFormPageModel):
        """"Проверка, что текст введенный ранее в форме, иммется в таблице"""
        self.check_element_have_text(PracticeFormPageLocators.MODAL_TITLE, Constants.TEXT)
        self.cells_of_row(index=0, locator=PracticeFormPageLocators.TABLE, locator_2=PracticeFormPageLocators.LINE,
                          locator_3=PracticeFormPageLocators.ELEMENTS_ON_LINE,
                          text='Student Name', text_2='Ivan Ivanov')
        self.cells_of_row(index=1, locator=PracticeFormPageLocators.TABLE, locator_2=PracticeFormPageLocators.LINE,
                          locator_3=PracticeFormPageLocators.ELEMENTS_ON_LINE,
                          text='Student Email', text_2=data.user_email)
        self.cells_of_row(index=2, locator=PracticeFormPageLocators.TABLE, locator_2=PracticeFormPageLocators.LINE,
                          locator_3=PracticeFormPageLocators.ELEMENTS_ON_LINE,
                          text='Gender', text_2=data.gender)
        self.cells_of_row(index=3, locator=PracticeFormPageLocators.TABLE, locator_2=PracticeFormPageLocators.LINE,
                          locator_3=PracticeFormPageLocators.ELEMENTS_ON_LINE,
                          text='Mobile', text_2=data.user_number)
        self.cells_of_row(index=4, locator=PracticeFormPageLocators.TABLE, locator_2=PracticeFormPageLocators.LINE,
                          locator_3=PracticeFormPageLocators.ELEMENTS_ON_LINE,
                          text='Date of Birth', text_2=f"{'15'} {'February'},{data.year}")
        self.cells_of_row(index=5, locator=PracticeFormPageLocators.TABLE, locator_2=PracticeFormPageLocators.LINE,
                          locator_3=PracticeFormPageLocators.ELEMENTS_ON_LINE,
                          text='Subjects', text_2=data.subjects)
        self.cells_of_row(index=6, locator=PracticeFormPageLocators.TABLE, locator_2=PracticeFormPageLocators.LINE,
                          locator_3=PracticeFormPageLocators.ELEMENTS_ON_LINE,
                          text='Hobbies', text_2=data.hobbies)
        self.cells_of_row(index=7, locator=PracticeFormPageLocators.TABLE, locator_2=PracticeFormPageLocators.LINE,
                          locator_3=PracticeFormPageLocators.ELEMENTS_ON_LINE,
                          text='Picture', text_2='my_photo.jpg')
        self.cells_of_row(index=8, locator=PracticeFormPageLocators.TABLE, locator_2=PracticeFormPageLocators.LINE,
                          locator_3=PracticeFormPageLocators.ELEMENTS_ON_LINE,
                          text='Address', text_2=data.current_address)
        self.cells_of_row(index=9, locator=PracticeFormPageLocators.TABLE, locator_2=PracticeFormPageLocators.LINE,
                          locator_3=PracticeFormPageLocators.ELEMENTS_ON_LINE,
                          text='State and City', text_2=f"{'Haryana'} {data.city}")
        #self.check_element_have_text(PracticeFormPageLocators.MODAL_FORM_STUDENT_INFO, 'Ivan Ivanov')
        #self.check_element_have_text(PracticeFormPageLocators.MODAL_FORM_STUDENT_INFO, data.user_email)
        #self.check_element_have_text(PracticeFormPageLocators.MODAL_FORM_STUDENT_INFO, data.gender)
        #self.check_element_have_text(PracticeFormPageLocators.MODAL_FORM_STUDENT_INFO, data.user_number)
        #self.check_element_have_text(PracticeFormPageLocators.MODAL_FORM_STUDENT_INFO,
                                     #f"{'15'} {'February'},{data.year}")
        #self.check_element_have_text(PracticeFormPageLocators.MODAL_FORM_STUDENT_INFO, data.subjects)
        #self.check_element_have_text(PracticeFormPageLocators.MODAL_FORM_STUDENT_INFO, data.hobbies)
        #self.check_element_have_text(PracticeFormPageLocators.MODAL_FORM_STUDENT_INFO, 'my_photo.jpg')
        #self.check_element_have_text(PracticeFormPageLocators.MODAL_FORM_STUDENT_INFO, data.current_address)
        #self.check_element_have_text(PracticeFormPageLocators.MODAL_FORM_STUDENT_INFO, f"{'Haryana'} {data.city}"),

    def choose_image_file(self, image_file):
        self.load_file(PracticeFormPageLocators.UPLOADPICTURE, image_file)

    def fill_date_form(self, data: PracticeFormPageModel):
        self.click_element(PracticeFormPageLocators.DATE_FORM)
        element_month = self.find_element(PracticeFormPageLocators.MONTH)
        element_year = self.find_element(PracticeFormPageLocators.YEAR)
        SelectList(element_month).select_by_value(data.month)
        SelectList(element_year).select_by_value(data.year)
        self.click_element(PracticeFormPageLocators.DAY)

    def click_on_button_close(self):
        self.click_element(PracticeFormPageLocators.BUTTON_CLOSE_MODAL_FORM)
