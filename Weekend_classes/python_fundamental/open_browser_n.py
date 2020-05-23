from selenium import webdriver
#import time
from time import sleep

def open_chrome_browser():
    driver = webdriver.Chrome(executable_path = "C://Users//Kamini//workspace_python//drivers//chromedriver.exe")
    driver.get("https://www.amazon.in")
    searchbox = driver.find_element_by_id("twotabsearchtextbox")
    searchbox.send_keys("Mackbook Pro")

    searchIcon = driver.find_element_by_class_name('nav-input')
    searchIcon.click()

    #To find element using linktext

  #  macbook_pro_details = driver.find_element_by_link_text('Apple MacBook Air (13-inch, 8GB RAM, 128GB Storage, 1.8GHz Intel Core i5) - Silver')
   # macbook_pro_details.click()

    macbook_pro_details = driver.find_element_by_partial_link_text('Apple MacBook Air')
    macbook_pro_details.click()

    link = driver.find_element_by_tag_name('a')
    print(link)
    print(link.text)

    list_of_link = driver.find_elements_by_tag_name('a')
    #print(list_of_link)
    for link in list_of_link:
        print(link.text)

    sleep(5)
    driver.close()

open_chrome_browser()
"""

def open_firefox_browser():
    driver = webdriver.Firefox(executable_path = "C:/Users/Kamini/workspace_python/drivers/geckodriver.exe")
    driver.get("https://www.amazon.in")
    driver.close()

open_firefox_browser()
"""