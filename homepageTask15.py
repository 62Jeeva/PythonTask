from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By

from Task15DDT.basepageTask15 import Basepage

class HomePage(Basepage):

    HOMEPAGE_DASHBOARD = (By.XPATH,"//h6[text()='Dashboard']")
    PROFILE = (By.XPATH,"//span[@class='oxd-userdropdown-tab']")
    LOGOUT = (By.XPATH,"//a[text() ='Logout']")


    def login(self):
        try:
          return self.wait.until(EC.visibility_of_element_located(self.HOMEPAGE_DASHBOARD)).is_displayed()
        except TimeoutException:
            return False

    def logout(self):
        self.wait.until(EC.element_to_be_clickable(self.PROFILE)).click()
        self.wait.until(EC.element_to_be_clickable(self.LOGOUT)).click()


    def close_browseroperation(self):
        self.close_browser()
