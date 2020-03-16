from selenium.webdriver.support.select import Select

class FormInputData:
    def __init__(self, driver):
        self.driver = driver
        self.first_name_input ='first_name'
        self.last_name_input ='last_name'
        self.email_input ='email'
        self.phone_input ='phone'
        self.address_input ='address'
        self.city_input ='city'
        self.state_input='state'
        self.zip_input ='zip'
        self.site_input ='website'
        self.hosting_input ='hosting'
        self.comments_input ='comment'
        self.button_click ="//button[@type='submit']"

    def set_name(self,name):
        self.driver.find_element_by_name (self.first_name_input).send_keys(name)

    def set_surname(self, surname):
        self.driver.find_element_by_name (self.last_name_input).send_keys(surname)

    def set_email(self, email_address):
        self.driver.find_element_by_name (self.email_input) .send_keys(email_address)

    def set_phone_numb(self, phone_number):
        self.driver.find_element_by_name (self.phone_input).send_keys(phone_number)

    def set_address(self, address):
        self.driver.find_element_by_name (self.address_input).send_keys(address)

    def set_city(self, city_name):
        self.driver.find_element_by_name (self.city_input).send_keys (city_name)

    def set_state(self, state_city):
        self.state_choice = Select(self.driver.find_element_by_name (self.state_input))
        self.state_choice.select_by_visible_text (state_city)

    def set_zip_code(self, zipcode):
        self.driver.find_element_by_name (self.zip_input).send_keys (zipcode)

    def website_input(self, website_addr):
        self.driver.find_element_by_name (self.site_input).send_keys (website_addr)

    def set_hosting_choice(self):
        self.driver.find_element_by_name (self.hosting_input).click()

    def comment_input(self, comment):
        self.driver.find_element_by_name (self.comments_input).send_keys (comment)

    def btn_click(self):
        self.driver.find_element_by_xpath (self.button_click).click ()







