

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Enter_page(Base):

    url = 'https://www.supertabak.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    age_no_18 = "/html/body/div[6]/div/div/div/a[2]"

    # Getters

    def get_age_no_18(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.age_no_18)))


    # Actions

    def click_age_no_18(self):
        self.get_age_no_18().click()
        print('Click age no 18')

    # Methods

    def age_control(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.click_age_no_18()
        self.get_current_url()
        self.assert_url("https://www.google.com/")




