from pagestask14.homepagetask14 import HomePage
from pagestask14.loginpagetask14 import LoginPage
from driver_setup import get_driver


def test_successful_login():
    driver = get_driver()
    home = HomePage(driver)
    login = LoginPage(driver)
    login.open_login_page()
    login.login("gvajk625@gmail.com","Jeeva@123")
    assert home.verify_login()
    home.perform_operation()
    home.close_browseroperation()

def test_invalid_email():
    driver = get_driver()
    home = HomePage(driver)
    try:
        login = LoginPage(driver)
        login.open_login_page()
        login.enter_text(login.EMAIL,"12312112")
        assert "email address" in login.invalid_email_message()
    finally:
        home.close_browseroperation()

def test_invalid_credentials():
    driver = get_driver()
    home = HomePage(driver)
    try:
        login = LoginPage(driver)
        login.open_login_page()
        login.login("abc@gmail.com","password123")
        assert login.invalid_email_password() =="Incorrect Email or Password"

    finally:
        home.close_browseroperation()

def test_username_field_neg():
    driver = get_driver()
    home = HomePage(driver)
    try:
        login = LoginPage(driver)
        login.open_login_page()
        assert login.validate_username("2323dsd233") == "gvajk625@gmail.com"
    finally:
        home.close_browseroperation()


def test_password_field():
    driver = get_driver()
    home = HomePage(driver)
    try:
        login = LoginPage(driver)
        login.open_login_page()
        assert login.validate_password("Jeeva@123") == "Jeeva@123"
    finally:
        home.close_browseroperation()

def test_login_button():
    driver = get_driver()
    home = HomePage(driver)
    try:
        login = LoginPage(driver)
        login.open_login_page()
        assert login.login_button_enabled()
    finally:
        home.close_browseroperation()


def test_logout():
    driver = get_driver()
    home = HomePage(driver)
    try:
       login = LoginPage(driver)
       login.open_login_page()
       login.login("gvajk625@gmail.com","Jeeva@123")
       assert home.verify_login()
       home.logout()
       assert home.verify_logout()
    finally:

       home.close_browseroperation()
