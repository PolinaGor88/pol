### Shop: отображение страницы товара ###
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

tab_Shop = driver.find_element_by_id('menu-item-40')
tab_Shop.click()

book_HTML5_Forms = driver.find_element_by_css_selector('.post-181 h3')
book_HTML5_Forms.click()

# book_title = driver.find_element_by_css_selector('.product_title.entry-title')
# book_title_expected_text = "HTML5 Forms"
# book_title = book_title.text
# if book_title == book_title_expected_text:
#     print("Текст совпадает:", book_title)
# else:
#     print("Фактический текст:", book_title)
#     print("Ожидаемый текст:", book_title_expected_text)

book_title_text = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".product_title.entry-title"), "HTML5 Forms"))

driver.quit()


### Shop: количество товаров в категории ###
from selenium import webdriver

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

tab_Shop = driver.find_element_by_id('menu-item-40')
tab_Shop.click()

category_HTML = driver.find_element_by_css_selector('.cat-item.cat-item-19 a')
category_HTML.click()

number_in_category = driver.find_elements_by_css_selector(".products.masonry-done li")
if len(number_in_category) == 3:
    print("В категории 3 товара")
else:
    print("Ошибка. Количество товаров в категории: " + str(len(number_in_category)))

driver.quit()


# ## Shop: сортировка товаров ###
from selenium import webdriver
from selenium.webdriver.support.select import Select

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

tab_Shop = driver.find_element_by_id('menu-item-40')
tab_Shop.click()

selector = driver.find_element_by_tag_name('[selected="selected"]')
selector_default = selector.get_attribute('text')
if selector_default == 'Default sorting':
    print('Выбрано значение Default sorting')
else:
    print('Выбрано другое значение: ',selector_default)

sorting_high_to_low = driver.find_element_by_class_name('orderby')
select = Select(sorting_high_to_low)
select.select_by_visible_text('Sort by price: high to low')

selector = driver.find_element_by_tag_name('[selected="selected"]')

selector_high_to_low = selector.get_attribute('text')
if selector_high_to_low == 'Sort by price: high to low':
    print('Выбрано значение: Sort by price: high to low')
else:
    print('Выбрано другое значение: ',selector_high_to_low)

driver.quit()


### Shop: отображение, скидка товара ###
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

tab_Shop = driver.find_element_by_id('menu-item-40')
tab_Shop.click()

book_Android_Quick = driver.find_element_by_class_name('post-169')
book_Android_Quick.click()

book_old_price = driver.find_element_by_css_selector('.price > del > span')
book_old_price_text = book_old_price.text
assert book_old_price_text == '₹600.00'

book_new_price = driver.find_element_by_css_selector('.price > ins > span')
book_new_price_text = book_new_price.text
assert book_new_price_text == '₹450.00'

Wait = WebDriverWait(driver, 5)
book_cover = Wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'.images')))
book_cover.click()

book_cover_close = Wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'.pp_close')))
book_cover_close.click()

driver.quit()
