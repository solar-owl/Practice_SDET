from conftest import form_fields_page
from selenium.common import UnexpectedAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_successful_form_fields(form_fields_page):

    #Заполнение полей name и password
    form_fields_page.fill_name('name')
    form_fields_page.fill_password('qwerty')

    #Выбор Milk и Coffee из списка What is your favorite drink?
    form_fields_page.select_checkbox('Milk')
    form_fields_page.select_checkbox('Coffee')

    # Выбор Yellow из списка What is your favorite color?
    form_fields_page.select_radio('Yellow')

    # Выбор Yes из списка Do you like automation?
    form_fields_page.select_dropdown('yes')

    #Добавление количества инструментов и инструмента с max количеством символов
    form_fields_page.add_message()

    #Заполнение поля email
    form_fields_page.fill_email('name@example.com')

    try:
        # Нажать на кнопку Submit
        form_fields_page.submit_form()
        # Ожидайте появления алерта
        alert_text = WebDriverWait(form_fields_page.driver, 20).until(
            EC.alert_is_present()
        )
    except UnexpectedAlertPresentException as e:
        # Обработка исключения
        alert_text = e.msg.split(": ")[2]  # Извлечение текста алерта из сообщения исключения
        alert_text = alert_text.split("}")[0]
    assert alert_text == "Message received!"
