from selenium import webdriver
from selenium.webdriver.common.by import By


def test_parent_xpath():

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.guvi.in/")

    live_classes_parent = driver.find_element(By.XPATH,"//p[text() = 'LIVE Classes']/parent::div[1]")
    courses_parent = driver.find_element(By.XPATH, "(//p[contains(text(),'Courses')])[1]/parent::div[1]")
    practice_parent = driver.find_element(By.XPATH,"(//p[contains(text(),'Practice')])[1]/parent::div[1]")
    resources_parent = driver.find_element(By.XPATH,"(//p[text() = 'Resources'])[1]/parent::div[1]")
    our_product_parent = driver.find_element(By.XPATH,"(//p[text() = 'Our Products'])[1]/parent::div[1]")
    driver.quit()

def test_child_xpath():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.guvi.in/")
    #live_classes_child = driver.find_element(By.XPATH,"(//p[text()='LIVE Classes']/parent::div/child::p)[1]")
    live_classes_child = driver.find_element(By.XPATH,"(//div[@id='solutions']/child::p)[1]")
    courses_child = driver.find_element(By.XPATH, "(//div[@id='solutions']/child::p)[2]")
    practice_child = driver.find_element(By.XPATH,"(//div[@id='solutions']/child::p)[3]")
    resources_child = driver.find_element(By.XPATH,"(//div[@id='solutions']/child::p)[4]")
    our_product_child = driver.find_element(By.XPATH, "(//div[@id='solutions']/child::p)[5]")
    driver.quit()

def test_sibling_xpath():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.guvi.in/")

    live_class_sibling = driver.find_elements(By.XPATH,"//p[text()='LIVE Classes']/following-sibling::*")
    courses_sibling = driver.find_elements(By.XPATH,"//p[text()='Courses']/following-sibling::*")
    practice_sibling = driver.find_element(By.XPATH,"//p[text()='Practice']/following-sibling::*")
    resources_sibling = driver.find_element(By.XPATH,"//p[text()='Resources']/following-sibling::*")
    ourproduct_sibling = driver.find_element(By.XPATH, "//p[text()='Our Products']/following-sibling::*")

    driver.quit()

def test_ancestor_xpath():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.guvi.in/")
    live_class_ancestor= driver.find_elements(By.XPATH,"(//p[contains(text(),'LIVE Classes')])[1]/ancestor::*")
    courses_ancestor = driver.find_elements(By.XPATH,"(//p[contains(text(),'Courses')])[1]/ancestor::*")
    practice_ancestor = driver.find_elements(By.XPATH,"(//p[contains(text(),'Practice')])[1]/ancestor::*")
    resources_ancestor = driver.find_elements(By.XPATH,"(//p[contains(text(),'Resources')])[1]/ancestor::*")
    our_product_ancestor=driver.find_elements(By.XPATH,"(//p[contains(text(),'Our Products')])[1]/ancestor::*")
    driver.quit()

def test_preceding_xpath():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.guvi.in/")
    live_class_preceding = driver.find_elements(By.XPATH,"(//p[contains(text(),'LIVE Classes')])[1]/preceding-sibling::*")
    courses_preceding = driver.find_elements(By.XPATH, "(//p[contains(text(),'Courses')])[1]/preceding-sibling::*")
    practice_preceding = driver.find_elements(By.XPATH,"(//p[contains(text(),'Practice')])[1]/preceding-sibling::*")
    resources_preceding = driver.find_elements(By.XPATH,"(//p[contains(text(),'Resources')])[1]/preceding-sibling::*")
    our_product_preceding = driver.find_elements(By.XPATH, "(//p[contains(text(),'Our Products')])[1]/preceding-sibling::*")
    driver.quit()


