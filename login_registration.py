### Registration_login: регистрация аккаунта ###
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://practice.automationtesting.in/")

tab_My_Account = driver.find_element_by_link_text('My Account')
tab_My_Account.click()

field_Email = driver.find_element_by_id('reg_email')
field_Email.send_keys('pol@mail.ru')

field_Password = driver.find_element_by_id('reg_password')
field_Password.send_keys('polina08anilop')

Register_btn = driver.find_element_by_css_selector('.woocomerce-FormRow .woocommerce-Button')
Register_btn.click()

driver.quit()


### Registration_login: логин в систему ###
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://practice.automationtesting.in/")

tab_My_Account = driver.find_element_by_link_text('My Account')
tab_My_Account.click()

field_Email = driver.find_element_by_id('username')
field_Email.send_keys('pol@mail.ru')

field_Password = driver.find_element_by_id('password')
field_Password.send_keys('polina08anilop')

Login_btn = driver.find_element_by_tag_name('[name="login"]')
Login_btn.click()

# element_Logout = driver.find_element_by_css_selector('.woocommerce-MyAccount-navigation-link--customer-logout a')
# if element_Logout is not None:
#     print('на странице есть элемент Logout')
# else:
#     print('на странице нет элемента Logout')

element_Logout_text = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce-MyAccount-navigation-link--customer-logout a"), "Logout"))

driver.quit()
