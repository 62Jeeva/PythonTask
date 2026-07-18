from selenium.webdriver.support.wait import WebDriverWait

class Basepage:

    def __init__(self,driver):
        self.driver=driver
        self.wait = WebDriverWait(driver,timeout=20,poll_frequency=2)


    def open_url(self,url):
        self.driver.get(url)
