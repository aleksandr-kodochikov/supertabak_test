from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Main_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    sidebar_tobacco = "//*[@id='sidebarNavigation']/ul/li[2]/a"
    sidebar_tobacco_tube = "//*[@id='sidebarNavigation']/ul/li[2]/div/ul/li[1]"
    slider_low = "//*[@id='slider_153']/span[1]"
    filter_slicing = "//span[@data-for='arrFilter_107_3400593401']"
    filter_produce = "//span[@data-for='arrFilter_104_2188530942']"
    filter_volume = "//span[@data-for='arrFilter_108_1462301370']"
    filter_set_tobacco = "//input[@id='set_filter']"
    add_to_cart_product_2 = "//*[@id='bx_1245396150_75802']/div[3]/a/span"
    name_product_2 = "//*[@id='bx_1245396150_75802']/div[2]/a"


    # Getters

    def get_sidebar_tobacco(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.sidebar_tobacco)))

    def get_sidebar_tobacco_tube(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.sidebar_tobacco_tube)))

    def get_slider_low(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.slider_low)))

    def get_filter_slicing(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_slicing)))

    def get_filter_produce(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_produce)))

    def get_filter_volume(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_volume)))

    def get_filter_set_tobacco(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_set_tobacco)))

    def get_add_to_cart_product_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_to_cart_product_2)))


    # Actions

    def move_to_sidebar_tobacco(self):
        self.driver.execute_script("window.scrollTo(0, 0)")
        ActionChains(self.driver).move_to_element(self.get_sidebar_tobacco()).perform()
        print('Move To Sidebar')

    def click_sidebar_tobacco_tube(self):
        ActionChains(self.driver).move_to_element(self.get_sidebar_tobacco_tube()).perform()
        self.get_sidebar_tobacco_tube().click()
        print('Click Sidebar Tobacco Tube')

    def set_slider_low(self):
        ActionChains(self.driver).click_and_hold(self.get_slider_low()).move_by_offset(80, 0).release().perform()
        print('Set Slider Low Price')

    def click_select_filter_slicing(self):
        self.get_filter_slicing().click()
        print('Click Select Slicing')

    def click_select_filter_produce(self):
        self.get_filter_produce().click()
        print('Click Select Produce')

    def click_select_filter_volume(self):
        self.get_filter_volume().click()
        print('Click Select Volume')

    def click_filter_set_tobacco(self):
        self.get_filter_set_tobacco().click()
        print('Click Filter Set Tobacco')

    def click_add_to_cart_product_2(self):
        self.get_add_to_cart_product_2().click()
        print('Add to cart product 2')

    def save_name_product_2(self):
        name_product_2_text = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.name_product_2)))
        global value_name_product_2_text
        value_name_product_2_text = name_product_2_text.text
        return value_name_product_2_text

    # Methods

    def select_products_2(self):
        self.get_current_url()
        self.move_to_sidebar_tobacco()
        self.click_sidebar_tobacco_tube()
        self.set_slider_low()
        self.click_select_filter_slicing()
        self.click_select_filter_produce()
        self.click_select_filter_volume()
        self.click_filter_set_tobacco()
        self.click_add_to_cart_product_2()





