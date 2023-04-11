

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Catalog_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    catalog_button = "//*[@id='horizontal-multilevel-menu']/li[2]/a"
    smoking_pipes = "//*[@id='js']/body/table/tbody/tr[2]/td[2]/div[2]/div[4]/div[1]/div[2]/div[1]/a"
    filter_price_pipe_min = "//input[@id='arrFilter_P1_MIN']"
    filter_price_pipe_max = "//input[@id='arrFilter_P1_MAX']"
    filter_brand_pipe = "//span[@data-for='arrFilter_86_329487895']"
    filter_material_pipe = "//*[@id='kombox-filter']/form/ul/li[7]/div[1]"
    select_material_pipe = "//span[@data-for='arrFilter_89_2895811748']"
    filter_mouthpiece_pipe = "//*[@id='kombox-filter']/form/ul/li[8]/div[1]"
    select_mouthpiece_pipe = "//span[@data-for='arrFilter_90_1117058440']"
    filter_length_pipe = "//*[@id='kombox-filter']/form/ul/li[9]/div[1]"
    select_length_pipe = "//span[@data-for='arrFilter_95_4005954217']"
    filter_handmade_pipe = "//*[@id='kombox-filter']/form/ul/li[13]/div[1]"
    select_handmade_pipe = "//span[@data-for='arrFilter_92_3157780942']"
    filter_country_pipe = "//*[@id='kombox-filter']/form/ul/li[15]/div[1]"
    select_country_pipe = "//span[@data-for='arrFilter_71_1688512129']"
    filter_set_pipe = "//input[@id='set_filter']"
    add_to_cart_pipe = "//*[@id='bx_1245396150_474230']/div[3]/a"
    name_product_1 = "//*[@id='bx_1245396150_474230']/div[2]/a"

    # Getters

    def get_catalog_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.catalog_button)))

    def get_smoking_pipes(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.smoking_pipes)))

    def get_filter_price_pipe_min(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_price_pipe_min)))

    def get_filter_price_pipe_max(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_price_pipe_max)))

    def get_filter_brand_pipe(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_brand_pipe)))

    def get_filter_material_pipe(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_material_pipe)))

    def get_select_material_pipe(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_material_pipe)))

    def get_filter_mouthpiece_pipe(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_mouthpiece_pipe)))

    def get_select_mouthpiece_pipe(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_mouthpiece_pipe)))

    def get_filter_length_pipe(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_length_pipe)))

    def get_select_length_pipe(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_length_pipe)))

    def get_filter_handmade_pipe(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_handmade_pipe)))

    def get_select_handmade_pipe(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_handmade_pipe)))

    def get_filter_country_pipe(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_country_pipe)))

    def get_select_country_pipe(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_country_pipe)))

    def get_filter_set_pipe(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_set_pipe)))

    def get_add_to_cart_pipe(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_to_cart_pipe)))

    # Actions

    def click_catalog_button(self):
        self.get_catalog_button().click()
        print('Click Catalog')

    def click_smoking_pipes(self):
        self.get_smoking_pipes().click()
        print('Click Smoking Pipes')

    def input_filter_price_pipe_min(self, price_min):
        self.get_filter_price_pipe_min().send_keys(price_min)
        print('Input Price Min')

    def input_filter_price_pipe_max(self, price_max):
        self.get_filter_price_pipe_max().send_keys(price_max)
        print('Input Price Max')

    def click_filter_brand_pipe(self):
        self.get_filter_brand_pipe().click()
        print('Click Filter Brand Pipe')

    def click_filter_material_pipe(self):
        self.get_filter_material_pipe().click()

    def click_select_material_pipe(self):
        self.get_select_material_pipe().click()
        print('Click Select Material Pipe')

    def click_filter_mouthpiece_pipe(self):
        self.get_filter_mouthpiece_pipe().click()

    def click_select_mouthpiece_pipe(self):
        self.get_select_mouthpiece_pipe().click()
        print('Click Select Mouthpiece Pipe')

    def click_filter_length_pipe(self):
        self.get_filter_length_pipe().click()

    def click_select_length_pipe(self):
        self.get_select_length_pipe().click()
        print('Click Select Length Pipe')

    def click_filter_handmade_pipe(self):
        self.get_filter_handmade_pipe().click()

    def click_select_handmade_pipe(self):
        self.get_select_handmade_pipe().click()
        print('Click Select Handmade Pipe')

    def click_filter_country_pipe(self):
        self.get_filter_country_pipe().click()

    def click_select_country_pipe(self):
        self.get_select_country_pipe().click()
        print('Click Select Country Pipe')

    def click_filter_set_pipe(self):
        self.get_filter_set_pipe().click()
        print('Click Filter Set Pipe')

    def click_add_to_cart_pipe(self):
        self.get_add_to_cart_pipe().click()
        print('Click Add To Cart Pipe')

    def save_name_product_1(self):
        name_product_1_text = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.name_product_1)))
        global value_name_product_1_text
        value_name_product_1_text = name_product_1_text.text
        return value_name_product_1_text



    # Methods

    def select_products_1(self):
        self.get_current_url()
        self.get_screenshot()
        self.click_catalog_button()
        self.click_smoking_pipes()
        self.input_filter_price_pipe_min('5000')
        self.input_filter_price_pipe_max('15000')
        self.click_filter_brand_pipe()
        self.click_filter_material_pipe()
        self.click_select_material_pipe()
        self.click_filter_mouthpiece_pipe()
        self.click_select_mouthpiece_pipe()
        self.click_filter_length_pipe()
        self.click_select_length_pipe()
        self.click_filter_handmade_pipe()
        self.click_select_handmade_pipe()
        self.click_filter_country_pipe()
        self.click_select_country_pipe()
        self.click_filter_set_pipe()
        self.click_add_to_cart_pipe()



