import time
import sys
from selenium.common import exceptions as ex
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def search_google():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com/")
    time.sleep(1)
    search = driver.find_element(By.NAME, "q").send_keys("tamil"+Keys.RETURN)

    # pages = len(driver.find_elements_by_class_name('SJajHc')) - 3
    i = 1

    while True:
        try:
            elems = driver.find_elements_by_xpath("//a[@href]")
            for elem in elems:
                if elem.get_attribute("href") == sys.argv[1]:
                    return i
            driver.find_element_by_id('pnnext').click()
            i = i + 1
        except ex.NoSuchElementException:
            return None
        
print("Searching..")
result = search_google()

if result:
    print(f'Found at page {result}')
else:
    print("Sorry no results found!")
