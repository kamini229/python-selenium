from selenium import webdriver
import time

def verify_search_functionality(search_text):
    driver = webdriver.Chrome()
    driver.get("https://www.flipkart.com")
    driver.maximize_window()
    time.sleep(4)

    driver.find_element_by_xpath("//button[@class='_2AkmmA _29YdH8']").click()

    search_box = driver.find_element_by_class_name("LM6RPg")
    search_box.send_keys(search_text)

    search_icon = driver.find_element_by_xpath("//button[@class='vh79eN']//*[local-name()='svg']")
    search_icon.click()
    time.sleep(5)

    #Assert
    search_product_info = driver.find_element_by_xpath("//span[@class='_2yAnYN']")
    search_product_info = search_product_info.text

    if(('result for "' + search_text + '"') in search_product_info):
        print("We have successfully searched the product " + search_text)
    else:
        print("the search product is not listed here")


    driver.close()
    driver.quit()

#verify_search_functionality("Mackbook pro")

verify_search_functionality("samsung mobile phone")
