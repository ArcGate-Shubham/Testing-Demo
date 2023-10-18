import time
import pytest
from selenium.webdriver.common.by import By
from PageObjects.LoginPage import Login
from PageObjects.DashboardPage import dashboard_data
from PageObjects.EmploymentStatusPage import EmpStatus
from Utilities.random_status import status_generator
from Utilities.logger import logclass
import configparser
config = configparser.ConfigParser()
config.read("Utilities/input.properties")


@pytest.mark.usefixtures("setup")
class Testlogin(logclass):
    def test_new_employement_status_add_with_correct_data(self):
        log = self.getthelogs()
        lg = Login(self.driver)
        db = dashboard_data(self.driver)
        es = EmpStatus(self.driver)
        log.info('TEST CASE, test_new_employement_status_add_with_correct_data')
        log.info('Test case starting')
        lg.input_username(config.get("credential", "correct_username"))
        log.info('entered username')
        lg.input_password(config.get("credential", "correct_password"))
        log.info('entered password')
        lg.click_login()
        log.info('click on login button')
        db.click_admin()
        log.info('click on admin section')
        time.sleep(2)
        db.click_job()
        log.info('click on job section')
        db.click_employement_status()
        log.info('click of employement status')
        Old_status_count = 0
        for i in es.total_status():
            Old_status_count = Old_status_count + 1
        es.click_add_button()
        log.info('click on add button for new status')
        es.input_new_status(status_generator())
        log.info('fill new employement status')
        es.click_savebutton()
        log.info('click on save button')
        New_Status_count = 0
        for j in es.total_status():
            New_Status_count = New_Status_count + 1

        if Old_status_count + 1 == New_Status_count:
            assert True
            log.info('Test Case pass')
        else:
            log.critical('Test Case fail')
            assert False

    def test_new_employement_status_add_with_blank_data(self):
        log = self.getthelogs()
        lg = Login(self.driver)
        db = dashboard_data(self.driver)
        es = EmpStatus(self.driver)
        log.info('TEST CASE, test_new_employement_status_add_with_blank_data')
        log.info('Test case starting')
        lg.input_username(config.get("credential", "correct_username"))
        log.info('entered username')
        lg.input_password(config.get("credential", "correct_password"))
        log.info('entered password')
        lg.click_login()
        log.info('click on login button')
        db.click_admin()
        log.info('click on admin section')
        time.sleep(2)
        db.click_job()
        log.info('click on job section')
        db.click_employement_status()
        log.info('click on employement status section')
        es.click_add_button()
        log.info('click on add button')
        self.driver.find_element(By.CSS_SELECTOR, 'form input.oxd-input').send_keys('')
        log.info('enterd blank data in input type')
        es.click_savebutton()
        log.info('click on save button ')
        time.sleep(3)
        if 'Required' in es.invalid_required_status():
            assert True
            log.info('Test case pass')
        else:
            log.critical("Test case fail")
            assert False

    def test_new_employement_status_add_with_exceed_limit_data(self):
        log = self.getthelogs()
        lg = Login(self.driver)
        db = dashboard_data(self.driver)
        es = EmpStatus(self.driver)
        log.info('TEST CASE, test_new_employement_status_add_with_exceed_limit_data')
        log.info('Test case starting')
        lg.input_username(config.get("credential", "correct_username"))
        log.info('entered username')
        lg.input_password(config.get("credential", "correct_password"))
        log.info('enetred password')
        lg.click_login()
        log.info('click on login button')
        db.click_admin()
        log.info('click on admin section')
        time.sleep(2)
        db.click_job()
        log.info('click on job section')
        db.click_employement_status()
        log.info('click on employeement status section')
        es.click_add_button()
        self.driver.find_element(By.CSS_SELECTOR, 'form input.oxd-input').send_keys('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
        log.info('fill exceed limit data')
        time.sleep(3)
        if 'Should not exceed 50 characters' in es.invalid_exceed_length():
            assert True
            log.info('Test case pass')
        else:
            log.critical('Test case fail')
            assert False
            
    def test_new_employement_status_deleted(self):
        log = self.getthelogs()
        lg = Login(self.driver)
        db = dashboard_data(self.driver)
        es = EmpStatus(self.driver)
        log.info("TEST CASE, test_new_employement_status_deleted")
        log.info('test case starting')
        lg.input_username(config.get("credential", "correct_username"))
        log.info('entered username')
        lg.input_password(config.get("credential", "correct_password"))
        log.info('entered password')
        lg.click_login()
        log.info('click on login button')
        db.click_admin()
        log.info('click on admin section')
        time.sleep(2)
        db.click_job()
        db.click_employement_status()
        log.info('click on employeement status section')
        Old_status_count = 0
        for i in es.total_status():
            Old_status_count = Old_status_count + 1
        es.click_delete_icon()
        log.info('Click on delete employeement icon')
        es.click_confirmation_box()
        log.info('click on confirmation box')
        time.sleep(4)
        New_Status_count = 0
        for j in es.total_status():
            New_Status_count = New_Status_count + 1
        
        if New_Status_count  == Old_status_count - 1:
            assert True
            log.info('Test case pass')
        else:
            log.critical('Test case fail')
            assert False
            
    def test_update_employement_status_with_correct_data(self):
        log = self.getthelogs()
        lg = Login(self.driver)
        db = dashboard_data(self.driver)
        es = EmpStatus(self.driver)
        log.info('TEST CASE, test_update_employement_status_with_correct_data')
        log.info('test case starting')
        lg.input_username(config.get("credential", "correct_username"))
        log.info('entered username')
        lg.input_password(config.get("credential", "correct_password"))
        log.info('enterd password')
        lg.click_login()
        log.info('click on login button')
        db.click_admin()
        log.info('click on admin section')
        time.sleep(2)
        db.click_job()
        log.info('click on job section')
        db.click_employement_status()
        log.info('click on employement section')
        Old_status_count = 0
        for i in es.total_status():
            Old_status_count = Old_status_count + 1
        es.click_update_icon()
        log.info('click on update icon of employement status')
        es.update_employeement_status(status_generator())
        log.info('update the employement status')
        es.click_savebutton()
        log.info('click on save button')
        New_Status_count = 0
        for j in es.total_status():
            New_Status_count = New_Status_count + 1

        if Old_status_count == New_Status_count:
            assert True
            log.info('Test case pass')
        else:
            log.critical('test case fail')
            assert False
         