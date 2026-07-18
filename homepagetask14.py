import time

from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By

from pagestask14.basepagetask14 import Basepage

class HomePage(Basepage):

    PROFILE_ICON=(By.XPATH,"(//img[@alt='Profile'])[1]")
    LOGOUT_BUTTON=(By.XPATH,"(//p[text() ='Sign Out']/ancestor::div[@id='signout'])[1]")
    HOME_LOGIN = (By.XPATH,"(//button[@id='login-btn'])[1]")
    #LOGOUT_BUTTON=(By.XPATH,"(//p[contains(text(),'Sign Out')])[1]")

    def verify_login(self):
        return self.wait.until(EC.visibility_of_element_located(self.PROFILE_ICON)).is_displayed()


    def perform_operation(self):
        print("Page Title: ",self.get_title())
        print("Current URL: ",self.get_current_url())

    def logout(self):
        self.click_element(self.PROFILE_ICON)
        self.wait.until(EC.element_to_be_clickable(self.LOGOUT_BUTTON)).click()
        print("After Logout URL:", self.get_current_url())

    def verify_logout(self):
        return self.is_displayed(self.HOME_LOGIN)
    
    def close_browseroperation(self):
        self.close_browser()
