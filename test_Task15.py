import datetime

from Task15DDT.excel_utility import Utility
from Task15DDT.homepageTask15 import HomePage
from Task15DDT.loginpageTask15 import LoginPage


excel_location = r"C:\Users\ADMIN\Documents\Task15excel.xlsx"

def test_excel_date(driver):
     home = HomePage(driver)
     login = LoginPage(driver)
     login.open_login_page()
     rows = Utility.row_count(excel_location)

     for row in range(2, rows + 1):

      username = Utility.read_excel_row(excel_location , row ,2)
      password = Utility.read_excel_row(excel_location , row ,3)
      login.enter_username(username)
      login.enter_password(password)
      login.click_login()

      current = datetime.datetime.now()
      Utility.write_excel_row(excel_location , row ,4,current.strftime("%d/%m/%Y"))
      Utility.write_excel_row(excel_location , row ,5,current.strftime("%H:%M:%S"))

      if home.login():
         Utility.write_excel_row(excel_location , row ,7,"TESTPASS")
         home.logout()
         login.open_login_page()

      else:
         Utility.write_excel_row(excel_location,row,7,"TESTFAIL")
         login.open_login_page()

