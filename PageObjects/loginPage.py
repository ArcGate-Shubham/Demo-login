from selenium.webdriver.common.by import By

class Login:
    def __init__(self, driver):
        self.driver = driver
        self.fill_input_for_firstname_xpath = '//input[@name="firstname"]'
        self.fill_input_for_lastname_xpath = '//input[@name="lastname"]'
        self.fill_input_for_email_xpath = '//input[@name="email"]'
        self.fill_input_for_password_xpath = '//input[@name="password"]'
        self.fill_confirmation_password_xpath = '//input[@name="password_confirmation"]'
        self.checked_first_checkbox_data_xpath = '//input[@name="tos"]'
        self.checked_second_checkbox_xpath = '//input[@name="newsletter"]'
        self.click_on_submit_button_xpath = "//span[@class='c290']"
        self.click_on_login_sytem_email_xpath = '//input[@name="identifier"]'
        self.click_on_sigin_button_xpath = '//*[@id="identifierNext"]/div/button/span'
        self.click_on_login_system_password_xpath = '//input[@jsname="YPqjbf"]'
        self.click_on_submit_button_xpath = '//*[@id="passwordNext"]/div/button/span'
        self.click_on_two_step_submit_button_xpath = 'div#totpNext button'
        self.verfiy_the_email_xpath = "//a[@aria-label='Sent']"
        self.click_on_link_activation_button_xpath = 'table tbody tr:nth-child(3) td div a'
        
    def input_first_name(self):
        self.driver.find_element(By.XPATH, self.fill_input_for_firstname_xpath).send_keys('login')
        
    def input_last_name(self):
        self.driver.find_element(By.XPATH, self.fill_input_for_lastname_xpath).send_keys('system')
        
    def input_email(self):
        self.driver.find_element(By.XPATH, self.fill_input_for_email_xpath).send_keys('loginsystem59@gmail.com')
        
    def input_password(self):
        self.driver.find_element(By.XPATH,self.fill_input_for_password_xpath).send_keys('Zxcvbn@111')
        
    def input_confirmation_password(self):
        self.driver.find_element(By.XPATH, self.fill_confirmation_password_xpath).send_keys('Zxcvbn@111')
        
    def checked_checkbox_first(self):
        self.driver.find_element(By.XPATH, self.checked_first_checkbox_data_xpath).click()
        
    def checked_checkbox_two(self):
        self.driver.find_element(By.XPATH, self.checked_second_checkbox_xpath).click()
        
    def click_on_submit_button(self):
        self.driver.find_element(By.XPATH, self.click_on_submit_button_xpath).click()
    
    def click_on_new_website_crediential(self):
        self.driver.find_element(By.XPATH,self.click_on_login_sytem_email_xpath).send_keys('loginsystem59@gmail.com')
        
    def click_on_sigin_button(self):
        self.driver.find_element(By.XPATH,self.click_on_sigin_button_xpath).click()
        
    def input_password_for_email_valid(self):
        self.driver.find_element(By.XPATH,self.click_on_login_system_password_xpath).send_keys('Zxcvbn@111')
        
    def click_submit_button_for_email_open(self):
        self.driver.find_element(By.XPATH,self.click_on_submit_button_xpath).click()
        
    def click_on_two_step_submit_button(self):
        self.driver.find_element(By.CSS_SELECTOR,self.click_on_two_step_submit_button_xpath).click()
        
    def verify_email_data(self):
        return self.driver.find_element(By.XPATH,self.verfiy_the_email_xpath).text
        
    def click_on_activation_link(self):
        self.driver.find_element(By.CSS_SELECTOR,self.click_on_link_activation_button_xpath).click()
