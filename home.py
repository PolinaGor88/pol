### Home: добавление комментария###
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://practice.automationtesting.in/")

driver.execute_script('window.scrollBy(0,600);')

Selenium_Ruby_btn = driver.find_element_by_tag_name('[href="https://practice.automationtesting.in/product/selenium-ruby/"]')
Selenium_Ruby_btn.click()

Reviews_btn = driver.find_element_by_tag_name('[href="#tab-reviews"]')
Reviews_btn.click()

star5 = driver.find_element_by_class_name('star-5')
star5.click()

field_Review = driver.find_element_by_id('comment')
field_Review.send_keys('Nice book!')

field_Name = driver.find_element_by_id('author')
field_Name.send_keys('Polina')

field_Email = driver.find_element_by_id('email')
field_Email.send_keys('pol@mail.ru')

Submit_btn = driver.find_element_by_id('submit')
Submit_btn.click()

driver.quit()