from selenium.webdriver.common.by import By

class Login:
    def __init__(self, driver):
        self.driver = driver
        self.textbox_username_xpath = 'username'
        self.textbox_password_xpath = 'password'
        self.button_login_xpath = 'orangehrm-login-button'
        self.text_invalid_msg_xpath = 'p.oxd-alert-content-text'
        self.text_invalid_required_xpath = 'form.oxd-form span'
    
    
    def input_username(self,Username):
        self.driver.find_element(By.NAME, self.textbox_username_xpath).send_keys(Username)
        
    def input_password(self, Password):
        self.driver.find_element(By.NAME, self.textbox_password_xpath).send_keys(Password)
        
    def click_login(self):
        self.driver.find_element(By.CLASS_NAME, self.button_login_xpath).click()
        
    def invalid_msg(self):
        return self.driver.find_element(By.CSS_SELECTOR,self.text_invalid_msg_xpath).text
    
    def invalid_required(self):
        return self.driver.find_element(By.CSS_SELECTOR,self.text_invalid_required_xpath).text
