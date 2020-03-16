from selenium import webdriver
from selenium.webdriver.support.select import Select

#CREATE WEBROWSER
driver = webdriver.Chrome(r'C:\Users\gonta\PycharmProjects\Selenium\seleniumddemo\chromedriver.exe')
driver.implicitly_wait(20)
driver.maximize_window()
driver.get('https://www.seleniumeasy.com/test/input-form-demo.html')

driver.find_element_by_name('first_name').send_keys('Oskar')
driver.find_element_by_name('last_name').send_keys('Kiteowy')
driver.find_element_by_name('email').send_keys('Kiteowy@gmail.com')
driver.find_element_by_name('phone').send_keys('111222333444')
driver.find_element_by_name('address').send_keys('Pogodna 11/18')
driver.find_element_by_name('city').send_keys('Bardo')
driver.find_element_by_name('state').click()

driver.find_element_by_name('zip').send_keys('50-421')
driver.find_element_by_name('website').send_keys('cba.pl')
driver.find_element_by_name('hosting').click()
driver.find_element_by_name('comment').send_keys('I have nothing to do')
driver.find_element_by_xpath("//button[@type='submit']").click()
