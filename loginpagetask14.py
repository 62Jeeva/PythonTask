from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pagestask14.basepagetask14 import Basepage


class LoginPage(Basepage):


    EMAIL=(By.ID,'email')
    PASSWORD=(By.ID,'password')
    LOGIN_BUTTON=(By.XPATH,"//a[@id='login-btn']")
    INVALID_EMAIL_PASSWORD = (By.XPATH,"(//div[contains(text(),'Incorrect Email or Password')])[1]")
    INVALID_EMAIL_MESSAGE = (By.XPATH,"//div[contains(@class,'invalid-feedback') and contains(text(),'doesnt look like an email address')]")


    def open_login_page(self):
        self.open_url("https://www.guvi.in/sign-in/?sourceUri=http%3A%2F%2Fwww.guvi.in%2F")
       # self.wait.until(EC.element_to_be_clickable(self.LOGIN))

    def login(self,email,password):
        self.enter_text(self.EMAIL,email)
        self.enter_text(self.PASSWORD,password)
        self.click_element(self.LOGIN_BUTTON)

    def validate_username(self, username):
        self.enter_text(self.EMAIL, username)
        return self.get_attribute(self.EMAIL, "value")

    def validate_password(self,password):
        self.enter_text(self.PASSWORD,password)
        return self.get_attribute(self.PASSWORD,"value")

    def login_button_enabled(self):
        return self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON)).is_enabled()

    def invalid_email_password(self):
        return self.get_text(self.INVALID_EMAIL_PASSWORD)

    def invalid_email_message(self):
        return self.get_text(self.INVALID_EMAIL_MESSAGE)