import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select


def verify_dynamic_dropdown():
    # ARRANGE

    driver = webdriver.Chrome()
    driver.get("https://www.flipkart.com/")
    driver.maximize_window()
    time.sleep(4)

    driver.find_element_by_xpath("//button[@class='_2AkmmA _29YdH8']").click();


    actions = ActionChains(driver)

    electronics = driver.find_element_by_xpath("//span[text()='Electronics']")

    actions.move_to_element(electronics).perform()

    samsung = driver.find_element_by_xpath("(//a[@title='Samsung'])[1]")

    # actions.move_to_element(samsung).click().perform()  # action chaining

    actions.move_to_element(samsung).perform()
    actions.click().perform()  # action chaining

    time.sleep(7)


verify_dynamic_dropdown()