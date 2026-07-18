from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Basepage:

    def __init__(self,driver):
        self.driver=driver
        self.wait = WebDriverWait(driver,timeout=20,poll_frequency=2)


    def open_url(self,url):
        self.driver.get(url)

    def close_browser(self):
        self.driver.quit()
