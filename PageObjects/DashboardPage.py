from selenium.webdriver.common.by import By

class dashboard_data:
    def __init__(self, driver):
        self.driver = driver
        self.textbox_dashboard_xpath = 'span h6'
        self.button_admin_xpath = "ul li a span"
        self.button_job_xpath = "//span[normalize-space()='Job']"
        self.button_employement_status_xpath = "ul.oxd-dropdown-menu li:nth-child(3) a"
        
    def dashboard(self):
        return self.driver.find_element(By.CSS_SELECTOR,self.textbox_dashboard_xpath).text
    
    def click_admin(self):
        self.driver.find_element(By.CSS_SELECTOR,self.button_admin_xpath).click()
    
    def click_job(self):
        self.driver.find_element(By.XPATH,self.button_job_xpath).click()
    
    def click_employement_status(self):
        self.driver.find_element(By.CSS_SELECTOR,self.button_employement_status_xpath).click()
