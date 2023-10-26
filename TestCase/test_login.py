import pytest      
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from Utilities.logger import logclass
from PageObjects.loginPage import Login



@pytest.mark.usefixtures("setup")
class Testlogin(logclass):
    def test_correct_username_correct_password(self):
        log = self.getthelogs()
        login = Login(self.driver)
        log.info("TEST CASE, test_correct_username_correct_password")
        log.info('Test Case Starting')
        login.input_first_name()
        login.input_last_name()
        login.input_email()
        login.input_password()
        login.input_confirmation_password()
        login.checked_checkbox_first()
        login.checked_checkbox_two()
          
        time.sleep(2)
        self.driver.execute_script("window.open('', '_blank');")
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(2)
        self.driver.get('https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox')
        
        login.click_on_new_website_crediential()
        login.click_on_sigin_button()
        time.sleep(5)
        login.input_password_for_email_valid()
        time.sleep(2)
        login.click_submit_button_for_email_open()
        time.sleep(2)
        
        
        time.sleep(2)
        if 'app' in login.verify_email_data():
            assert True
        else:
            assert False
