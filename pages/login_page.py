"""Модуль авторизации"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Login_page(Base):

    url = 'https://www.supertabak.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    user_name = "//input[@name='USER_LOGIN']"
    password = "//input[@name='USER_PASSWORD']"
    login_button = "//input[@name='Login']"
    login_name = "//*[@id='js']/body/table/tbody/tr[1]/td/table/tbody/tr/td[2]/div[1]/form/table/tbody/tr[1]/td"
    age_yes_18 = "/html/body/div[6]/div/div/div/a[1]"

    # Getters

    def get_user_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_name)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))

    def get_login_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_name)))

    def get_age_yes_18(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.age_yes_18)))

    # Actions

    def input_user_name(self, user_name):
        self.get_user_name().send_keys(user_name)
        print('Input user name')

    def input_password(self, password):
        self.get_password().send_keys(password)
        print('Input password')

    def click_login_button(self):
        self.get_login_button().click()
        print('Click Login button')

    def click_age_yes_18(self):
        self.get_age_yes_18().click()
        print('Click age yes 18')

    # Methods

    def authorization(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.click_age_yes_18()
        self.get_current_url()
        self.input_user_name("pythontest_sel")
        self.input_password("dhT3m7as9Krf")
        self.click_login_button()
        self.assert_login_name(self.get_login_name(), "pythontest_sel")



