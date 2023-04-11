from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Account_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    personal_account_button = "//a[@title='Личный кабинет']"
    main_word = "//*[@id='js']/body/table/tbody/tr[2]/td[2]/div[2]/div[2]/h1"
    edit_profile = "//*[@id='js']/body/table/tbody/tr[2]/td[2]/div[2]/div[2]/div/div[1]/div[2]/ul/li[1]/a"
    personal_section_link = "//*[@id='breadcrumb']/a[2]"
    cart_contain_button = "//*[@id='js']/body/table/tbody/tr[2]/td[2]/div[2]/div[2]/div/div[2]/div[1]/ul/li[1]/a"
    clear_cart = "//*[@id='basket_container']/form[2]/a"
    pay_delivery = "//*[@id='horizontal-multilevel-menu']/li[3]/a"
    link_about_shop = "//*[@id='horizontal-multilevel-menu']/li[4]/a"

    # Getters

    def get_personal_account_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.personal_account_button)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))

    def get_edit_profile(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.edit_profile)))

    def get_personal_section_link(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.personal_section_link)))

    def get_cart_contain_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_contain_button)))

    def get_clear_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.clear_cart)))

    def get_pay_delivery(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.pay_delivery)))

    def get_link_about_shop(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.link_about_shop)))

    # Actions

    def click_personal_account_button(self):
        self.get_personal_account_button().click()
        print('Enter Personal Account')

    def click_edit_profile(self):
        self.get_edit_profile().click()
        print('Click Edit Profile')

    def click_personal_section_link(self):
        self.get_personal_section_link().click()
        print('Click Personal Section Link')

    def click_cart_contain_button(self):
        self.get_cart_contain_button().click()
        print('Click Cart Contain Button')

    def click_clear_cart(self):
        try:
            self.get_clear_cart().click()
            print('Click Clear Cart')
        except TimeoutException as exception:
            print('Cart Empty')

    def click_link_pay_delivery(self):
        self.get_pay_delivery().click()
        print('Click Pay and Delivery Link')

    def click_link_about_shop(self):
        self.get_link_about_shop().click()
        print('Click link About Shop')


    # Methods

    def personal_account(self):
        self.get_current_url()
        self.click_personal_account_button()
        self.assert_word(self.get_main_word(), "ЛИЧНЫЙ КАБИНЕТ")
        self.click_edit_profile()
        self.get_screenshot()
        self.click_personal_section_link()
        self.click_cart_contain_button()
        self.get_screenshot()
        self.click_clear_cart()
        self.click_link_pay_delivery()
        self.click_link_about_shop()



