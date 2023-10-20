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
        self.job_description_validation_xpath = "//div[@class='oxd-layout-context']//div[2]//div[1]//span[1]"
        self.job_note_validation_xpath = "//div[4]//div[1]//span[1]"
        self.cancel_button_click_xpath = 'button.oxd-button--ghost'
        self.button_delete_job_title_xpath = '.bi-trash'
        self.button_confirmation_box_yes_xpath = 'button.orangehrm-button-margin:nth-child(2)'
        self.job_title_exceed_value = '3333333333333333333333333333333333333333333333333333333333333333333333333333333333353333333333333332d'
        self.job_description_exceed_value = 'ascascascascascaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaasasascascascascascaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaasasascascascascascaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaasasascascascascascaaaaggggggggggggc'
        
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
        self.driver.find_element(By.CSS_SELECTOR, self.add_new_job_title_xpath).send_keys(self.job_title_exceed_value)
        
    def exceed_limit_for_job_description(self):
        self.driver.find_element(By.XPATH,self.add_job_description_xpath).send_keys(self.job_description_exceed_value)
        
    def exceed_limit_for_note(self):
        self.driver.find_element(By.XPATH, self.add_new_add_note_xpath).send_keys(self.job_description_exceed_value)

    def job_description_required_validation(self):
        return self.driver.find_element(By.XPATH,self.job_description_validation_xpath).text
    
    def job_note_required_validation(self):
        return self.driver.find_element(By.XPATH,self.job_note_validation_xpath).text
    
    def click_on_cancel_button(self):
        self.driver.find_element(By.CSS_SELECTOR,self.cancel_button_click_xpath).click()
        
    def click_delete_job_title_button(self):
        self.driver.find_element(By.CSS_SELECTOR,self.button_delete_job_title_xpath).click()
        
    def click_confirmation_box_button_yes(self):
        self.driver.find_element(By.CSS_SELECTOR,self.button_confirmation_box_yes_xpath).click()