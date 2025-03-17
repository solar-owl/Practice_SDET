from conftest import form_fields_page
from selenium.common import UnexpectedAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

@allure.feature('Form Fields')
@allure.story('Existence alert with message')
def test_successful_form_fields(form_fields_page):
    with allure.step('Fill in the Name field'):
        form_fields_page.fill_name('name')
    with allure.step('Fill in the Password field'):
        form_fields_page.fill_password('qwerty')

    with allure.step('Choose Milk and Coffee from the What is your favorite drink list?'):
        form_fields_page.select_checkbox('Milk')
        form_fields_page.select_checkbox('Coffee')

    with allure.step('Choose Yellow from the What is your favorite color list?'):
        form_fields_page.select_radio('Yellow')

    with allure.step('Choose Yes from the Do you like automation list?'):
        form_fields_page.select_dropdown('yes')

    with allure.step('Add the number of tools and the tool with the maximum number of characters'):
        form_fields_page.add_message()

    with allure.step('Fill in the Email field'):
        form_fields_page.fill_email('name@example.com')

    with allure.step('Click Submit button'):
        try:
            form_fields_page.submit_form()
            # Ожидайте появления алерта
            alert_text = WebDriverWait(form_fields_page.driver, 20).until(
                EC.alert_is_present()
            )
        except UnexpectedAlertPresentException as e:
            # Обработка исключения
            alert_text = e.msg.split(": ")[2]  # Извлечение текста алерта из сообщения исключения
            alert_text = alert_text.split("}")[0]

    with allure.step('Check message'):
        assert alert_text == "Message received!"
