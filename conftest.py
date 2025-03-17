import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.form_fields_page import FormFieldsPage

@pytest.fixture(scope="function")
def driver():
    # Экземпляр драйвера
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    #  Перейдем по ссылке https://practice-automation.com/form-fields
    driver.get('https://practice-automation.com/form-fields')
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def form_fields_page(driver):
    return FormFieldsPage(driver)