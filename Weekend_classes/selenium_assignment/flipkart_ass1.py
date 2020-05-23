from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains


def flipkart_ass1():
    driver = webdriver.Chrome()
    driver.get("https://www.flipkart.com/")
    driver.maximize_window()
    time.sleep(4)

    driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[1]/input[1]").send_keys("kamini.pawar229@gmail.com")
    driver.find_element_by_xpath("//input[@type='password']").send_keys("Hridha@3")
    driver.find_element_by_xpath("//button[@class='_2AkmmA _1LctnI _7UHT_c']//span[contains(text(),'Login')]").click()
    time.sleep(5)

    actions = ActionChains(driver)

    electronics = driver.find_element_by_xpath("//span[text()='Electronics']")

    actions.move_to_element(electronics).perform()

    samsung = driver.find_element_by_link_text("Samsung")

    # actions.move_to_element(samsung).click().perform()  # action chaining

    actions.move_to_element(samsung).perform()
    actions.click().perform()  # action chaining

    time.sleep(7)

    driver.find_element_by_link_text("Samsung J8").click()
    element = driver.find_element_by_class_name("_35KyD6")
    print(element.text)
    driver.back()
    time.sleep(3)


    driver.find_element_by_link_text("Samsung On6").click()
    driver.back()
    time.sleep(3)

    driver.find_element_by_link_text("Galaxy A9").click()
    driver.back()
    time.sleep(3)

    driver.find_element_by_link_text("Samsung S9").click()
    driver.back()
    time.sleep(3)



flipkart_ass1()