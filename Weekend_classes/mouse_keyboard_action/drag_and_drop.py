import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select


def verify_drag_and_drop():
    # ARRANGE

    driver = webdriver.Chrome("/Users/gaurnitai/Desktop/PySeBootcamp/drivers/chromedriver")
    driver.get("https://jqueryui.com/draggable/")
    driver.maximize_window()
    time.sleep(4)

    driver.switch_to.frame(0)

    draggable = driver.find_element_by_id("draggable")
    print(draggable)

    actions = ActionChains(driver)
    actions.click_and_hold(draggable).drag_and_drop_by_offset(draggable, 100, 100).perform()

    time.sleep(5)

    driver.close()
    driver.quit()


verify_drag_and_drop()
