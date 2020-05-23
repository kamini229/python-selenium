import time

from selenium import webdriver


def verify_drag_and_drop():
    # ARRANGE

    driver = webdriver.Chrome("/Users/gaurnitai/Desktop/PySeBootcamp/drivers/chromedriver")
    driver.get("https://www.amazon.in")
    driver.maximize_window()
    time.sleep(4)

    search_box = driver.find_element_by_id("twotabsearchtextbox")  # Find the location of search box
    search_box.send_keys("Macbook pro")  # to enter text we have to use send_keys()

    # Finding xpath using contains(attribute, textwithinattributevalue)
    search_icon = driver.find_element_by_xpath("//input[@type='submit']")
    search_icon.click()

    time.sleep(5)

    parent_window = driver.current_window_handle
    print(parent_window)

    driver.find_element_by_xpath("(//a[@class='a-link-normal a-text-normal'])[1]").click()

    time.sleep(3)

    windows_set = driver.window_handles

    print(windows_set)

    for window in windows_set:
        if(window != parent_window):
            driver.switch_to.window(window)

    productTitle = driver.find_element_by_id("productTitle")
    print(productTitle.text)



    driver.switch_to.window(parent_window)

    time.sleep(3)

    driver.find_element_by_xpath("(//a[@class='a-link-normal a-text-normal'])[1]").click()


    time.sleep(9)


verify_drag_and_drop()
