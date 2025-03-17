import pytest
from selenium import webdriver
from pages.form_fields_page import FormFieldsPage

@pytest.fixture(scope="function")
def driver():
    # Экземпляр драйвера
    driver = webdriver.Chrome()
    #  Перейдем по ссылке https://practice-automation.com/form-fields
    driver.get('https://practice-automation.com/form-fields')
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def form_fields_page(driver):
    return FormFieldsPage(driver)