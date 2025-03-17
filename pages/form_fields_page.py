from selenium.common import UnexpectedAlertPresentException
from selenium.webdriver.common.alert import Alert

from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

NAME_INPUT = (By.ID, 'name-input')
PASSWORD_INPUT = (By.CSS_SELECTOR, 'input[type="password"]')
EMAIL_INPUT = (By.NAME, 'email')
LIST_TOOLS = (By.XPATH, '//label[contains(text(), "Automation tools")]/following-sibling::ul')
SUBMIT_BUTTON = (By.ID, 'submit-btn')
MESSAGE_INPUT = (By.ID, 'message')
DROPDOWN = (By.XPATH, '//select[@name="automation"]')
CHECKBOX_TEMPLATE = (By.XPATH, '//input[@type="checkbox" and @value="{}"]')
RADIO_TEMPLATE = (By.XPATH, '//input[@type="radio" and @value="{}"]')

class FormFieldsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def fill_name(self, name:str):
        self.find(NAME_INPUT).send_keys(name)

    def fill_password(self, password:str):
        self.find(PASSWORD_INPUT).send_keys(password)

    def fill_email(self, email:str):
        self.find(EMAIL_INPUT).send_keys(email)

    def select_checkbox(self, object):
        locator = (By.XPATH, CHECKBOX_TEMPLATE[1].format(object))
        self.find_to_click(locator).click()

    def select_radio(self, object):
        locator = (By.XPATH, RADIO_TEMPLATE[1].format(object))
        self.find_to_click(locator).click()

    def select_dropdown(self, value):
        self.find(DROPDOWN).send_keys(value)

    def add_message(self):
        tools = self.find(LIST_TOOLS).text
        elements_tools = tools.split('\n')
        longest_element = max(elements_tools, key=len)
        self.find(MESSAGE_INPUT).send_keys(str(len(elements_tools)) + ' ')
        self.find(MESSAGE_INPUT).send_keys(longest_element)

    def submit_form(self):
        self.find_to_click(SUBMIT_BUTTON).click()
