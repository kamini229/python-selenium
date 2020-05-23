import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys


def verify_drag_and_drop():
    # ARRANGE

    driver = webdriver.Chrome("/Users/gaurnitai/Desktop/PySeBootcamp/drivers/chromedriver")
    driver.get("https://www.google.com")
    driver.maximize_window()
    time.sleep(4)

    search_box = driver.find_element_by_name("q")

    # search_box.send_keys("Python")

    # search_box.send_keys(Keys.ENTER)

    time.sleep(3)

    actions = ActionChains(driver)

    # actions.move_to_element(search_box).send_keys(Keys.SHIFT).send_keys("python").send_keys("\ue007").perform()

    actions.key_down("\ue008", search_box).send_keys("python").key_up("\ue008", search_box).send_keys(
        "\ue007").perform()

    # actions.send_keys(Keys.ENTER).perform()

    # driver.find_element_by_name("btnK").click()

    time.sleep(3)


verify_drag_and_drop()