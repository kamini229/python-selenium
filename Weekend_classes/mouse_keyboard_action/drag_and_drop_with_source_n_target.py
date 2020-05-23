import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select


def verify_drag_and_drop():
    # ARRANGE

    driver = webdriver.Chrome("/Users/gaurnitai/Desktop/PySeBootcamp/drivers/chromedriver")
    driver.get("https://jqueryui.com/droppable/")
    driver.maximize_window()
    time.sleep(4)

    driver.switch_to.frame(0)

    source = driver.find_element_by_id("draggable")

    target = driver.find_element_by_id("droppable")

    actions = ActionChains(driver)
    actions.click_and_hold(source).drag_and_drop(source, target).perform()

    time.sleep(5)

    driver.close()
    driver.quit()


verify_drag_and_drop()