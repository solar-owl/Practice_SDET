from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find(self, args):
        return self.driver.find_element(*args)

    def find_to_click(self, args):
        element = self.driver.find_element(*args)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()
        # self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        # WebDriverWait(self.driver, 10).until(
        #     EC.element_to_be_clickable(args)
        # )
        return element