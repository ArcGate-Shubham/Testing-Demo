from selenium.webdriver.common.by import By

class jobtitle_data:
    def __init__(self, driver):
        self.driver = driver
        self.button_add_job_title_xpath = '.orangehrm-header-container button'
        self.add_new_job_title_xpath = "form div div div input"
        self.add_job_description_xpath = '//textarea[@placeholder="Type description here"]'
        self.add_new_image_upload_xpath = '//input[@type="file"]'
        self.add_new_add_note_xpath = '//textarea[@placeholder="Add note"]'
        self.save_new_job_title_xpath = '//button[@type="submit"]'
        self.total_job_title_xpath = "div.oxd-table-card"
        self.required_job_title_role_xpath = 'form span'
        
    def click_add_new_job_title(self):
        self.driver.find_element(By.CSS_SELECTOR, self.button_add_job_title_xpath).click()
        
    def input_new_job_title_role(self, Name):
        self.driver.find_element(By.CSS_SELECTOR, self.add_new_job_title_xpath).send_keys(Name)
        
    def input_job_description(self,Description):
        self.driver.find_element(By.XPATH, self.add_job_description_xpath).send_keys(Description)
        
    def input_image_upload(self):
        self.driver.find_element(By.XPATH, self.add_new_image_upload_xpath).send_keys('/home/arcgate/college-data.jpeg')
        
    def input_new_add_note(self, Note):
        self.driver.find_element(By.XPATH, self.add_new_add_note_xpath).send_keys(Note)
        
    def save_all_data_of_job_title(self):
        self.driver.find_element(By.XPATH, self.save_new_job_title_xpath).click()
        
    def total_job_title_data(self):
        return self.driver.find_elements(By.CSS_SELECTOR, self.total_job_title_xpath)
    
    def job_title_required_validation(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.required_job_title_role_xpath).text
    
    def exceed_limit_of_new_job_title(self):
        self.driver.find_element(By.CSS_SELECTOR, self.add_new_job_title_xpath).send_keys('3333333333333333333333333333333333333333333333333333333333333333333333333333333333353333333333333332d')
