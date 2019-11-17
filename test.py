from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Firefox()
print('### 打开浏览器')
driver.get("http://www.baidu.com")
print('### 打开网页')
# assert "Python" in driver.title
driver.title
elem = driver.find_element_by_name("wd")
elem.clear()

elem.send_keys("pycon")
elem.send_keys(Keys.ENTER)
assert "No results found." not in driver.page_source
# driver.close()