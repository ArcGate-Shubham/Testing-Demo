from selenium.webdriver.common.by import By

class EmpStatus:
    def __init__(self, driver):
        self.driver = driver
        self.button_add_status_xpath = "//button[normalize-space()='Add']"
        self.inputfield_name_xpath = "form input.oxd-input"
        self.total_field_xpath = "div.oxd-table-card"
        self.button_save_xpath = "button.oxd-button--secondary"
        self.required_emp_status_xpath = 'form span'
        self.button_delete_click_xpath = '.bi-trash'
        self.button_confirmation_box_xpath = 'button.orangehrm-button-margin:nth-child(2)'
        self.button_update_click_xpath = '.oxd-table-card div div:nth-child(3) div button:nth-child(2)'
        self.update_employeement_status_xpath = 'form input'
        
    def click_add_button(self):
        self.driver.find_element(By.XPATH, self.button_add_status_xpath).click()
        
    def input_new_status(self, Name):
        self.driver.find_element(By.CSS_SELECTOR, self.inputfield_name_xpath).send_keys(Name)
        
    def total_status(self):
        return self.driver.find_elements(By.CSS_SELECTOR, self.total_field_xpath)
        
    def click_savebutton(self):
        self.driver.find_element(By.CSS_SELECTOR,self.button_save_xpath).click()
        
    def invalid_required_status(self):
        return self.driver.find_element(By.CSS_SELECTOR,self.required_emp_status_xpath).text
    
    def invalid_exceed_length(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.required_emp_status_xpath).text
    
    def click_delete_icon(self):
        self.driver.find_element(By.CSS_SELECTOR,self.button_delete_click_xpath).click()
        
    def click_confirmation_box(self):
        self.driver.find_element(By.CSS_SELECTOR,self.button_confirmation_box_xpath).click()
        
    def click_update_icon(self):
        self.driver.find_element(By.CSS_SELECTOR,self.button_update_click_xpath).click()
        
    def update_employeement_status(self, Name):
        self.driver.find_element(By.CSS_SELECTOR,self.update_employeement_status_xpath).send_keys(Name)
        
    def update_clear_value_employeement_status(self):
        data = self.driver.find_element(By.CSS_SELECTOR,self.update_employeement_status_xpath)
        data.clear()
