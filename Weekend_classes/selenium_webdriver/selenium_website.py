from selenium import webdriver
from time import sleep

def test_documentation_link():
    driver = webdriver.Chrome()
    driver.get("https://www.selenium.dev/")
    sleep(4)


    # Absolute xpath
  #  driver.find_element_by_link_text("Downloads").click()

    # Relative xpath
    driver.find_element_by_xpath("(//a[@href='/downloads'])[1]").click()

    sleep(8)
    driver.find_element_by_xpath("(//a[@href='/documentation'])[1]").click()

   # xpath = driver.find_element_by_xpath("/html[1]/body[1]/header[1]/nav[1]/a[3]")
   # documentation = driver.find_element_by_link_text("documentation")
    #xpath.click()
    sleep(8)
    driver.quit()
    

test_documentation_link()