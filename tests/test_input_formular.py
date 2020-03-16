import pytest
from pages.formular import FormInputData
from selenium import webdriver

class Testformular:

    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome (r'C:\Users\gonta\PycharmProjects\Selenium\seleniumddemo\chromedriver.exe')
        self.driver.implicitly_wait (20)
        self.driver.maximize_window ()
        # yield
        # self.driver.quit()

    def test_input_formular(self, setup):
        self.driver.get ('https://www.seleniumeasy.com/test/input-form-demo.html')
        self.driver.implicitly_wait(40)
        input_formular = FormInputData(self.driver)
        input_formular.first_name_input('Oskar')
        input_formular.last_name_input('Kiteowy')
        input_formular.email_input('oskarowy@gmail.com')
        input_formular.phone_input('666555444')
        input_formular.address_input('Czaarna 11/18')
        input_formular.city_input('Kudowa Zdroj')
        input_formular.state_input('Georgia')
        input_formular.zip_input('50-123')
        input_formular.website_input('kite.cba.pl')
        input_formular.hosting_input()
        input_formular.comment_input("I have no comment yet")
        input_formular.btn_click()