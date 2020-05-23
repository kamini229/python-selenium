from selenium import webdriver
import time

def verify_search_functionality(search_text):
    driver = webdriver.Chrome()
    driver.get("https://www.snapdeal.com")
    driver.maximize_window()
    time.sleep(4)
    search_box = driver.find_element_by_name("keyword")
    search_box.send_keys(search_text)

    #finding xpathusing attribute
    search_icon = driver.find_element_by_xpath("//button[contains(@class, 'searchformButton')]")
   # search_icon = driver.find_element_by_xpath("//span[@class='searchTextSpan']")
    search_icon.click()
    time.sleep(5)

    search_product_info = driver.find_element_by_xpath("(//span[@class='nnn'])[1]")
    search_product_info = search_product_info.text

    if(search_product_info == "We've got 10000+ results for 'samsung mobile phone'"):
        print("We have successfully searched the product " + search_text)
    else:
        print("the search product is not listed here")


    driver.close()
    driver.quit()

verify_search_functionality("Mackbook pro")

verify_search_functionality("samsung mobile phone")
