from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from Task15DDT.basepageTask15 import Basepage

class LoginPage(Basepage):

    USERNAME=(By.XPATH,"//input[@name='username']")
    PASSWORD=(By.XPATH,"//input[@name='password']")
    lOGIN_BUTTON=(By.XPATH,"//button[@type='submit']")

    def open_login_page(self):
        self.open_url("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    def enter_username(self,username):
        self.wait.until(EC.visibility_of_element_located(self.USERNAME)).clear()
        self.driver.find_element(*self.USERNAME).send_keys(username)

    def enter_password(self,password):
        self.wait.until(EC.visibility_of_element_located(self.PASSWORD)).clear()
        self.driver.find_element(*self.PASSWORD).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.lOGIN_BUTTON).click()
