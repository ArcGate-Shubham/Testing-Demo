import time
import pytest
from selenium.webdriver.common.by import By
from PageObjects.LoginPage import Login
from PageObjects.DashboardPage import dashboard_data
from PageObjects.EmploymentStatusPage import EmpStatus
from PageObjects.JobTitlepage import jobtitle_data
from Utilities.random_status import status_generator
from Utilities.logger import logclass
import configparser
config = configparser.ConfigParser()
config.read("Utilities/input.properties")


@pytest.mark.usefixtures("setup")
class TestNewJobTitle(logclass):
    def test_new_job_title_with_correct_input_data(self):
        log = self.getthelogs()
        lg = Login(self.driver)
        db = dashboard_data(self.driver)
        es = jobtitle_data(self.driver)
        log.info('TEST CASE, test_new_job_title_with_correct_input_data')
        log.info('Test case starting')
        lg.input_username(config.get("credential", "correct_username"))
        lg.input_password(config.get("credential", "correct_password"))
        lg.click_login()
        db.click_admin()
        time.sleep(2)
        db.click_job()
        db.click_job_title_section()
        old_job_title = 0
        for i in es.total_job_title_data():
            old_job_title = old_job_title + 1   
        es.click_add_new_job_title()
        es.input_new_job_title_role(status_generator())
        es.input_job_description(status_generator())
        es.input_image_upload()
        es.input_new_add_note(status_generator())
        time.sleep(3)
        es.save_all_data_of_job_title()
        new_job_title = 0
        for j in es.total_job_title_data():
            new_job_title = new_job_title + 1
        if old_job_title + 1 == new_job_title:
            assert True
            log.info('Test Case Pass')
        else:
            log.critical('Test Case Fail')
            assert False
        
    def test_new_job_title_with_fill_only_job_title_role_another_field_blank_input(self):
        log = self.getthelogs()
        lg = Login(self.driver)
        db = dashboard_data(self.driver)
        es = jobtitle_data(self.driver)
        log.info('TEST CASE, test_new_job_title_with_fill_only_job_title_role_another_field_blank_input')
        log.info('Test case starting')
        lg.input_username(config.get("credential", "correct_username"))
        lg.input_password(config.get("credential", "correct_password"))
        lg.click_login()
        db.click_admin()
        time.sleep(2)
        db.click_job()
        db.click_job_title_section()
        old_job_title = 0
        for i in es.total_job_title_data():
            old_job_title = old_job_title + 1
        es.click_add_new_job_title()
        es.input_new_job_title_role(status_generator())
        es.save_all_data_of_job_title()
        new_job_title = 0
        for j in es.total_job_title_data():
            new_job_title = new_job_title + 1
        if old_job_title + 1 == new_job_title:
            assert True
            log.info('Test Case Pass')
        else:
            log.critical('Test Case Fail')
            assert False

    def test_new_job_title_with_blank_job_title_role_another_field_input_filled(self):
        log = self.getthelogs()
        lg = Login(self.driver)
        db = dashboard_data(self.driver)
        es = jobtitle_data(self.driver)
        log.info('TEST CASE, test_new_job_title_with_fill_only_job_title_role_another_field_blank_input')
        log.info('Test case starting')
        lg.input_username(config.get("credential", "correct_username"))
        lg.input_password(config.get("credential", "correct_password"))
        lg.click_login()
        db.click_admin()
        time.sleep(2)
        db.click_job()
        db.click_job_title_section()
        es.click_add_new_job_title()
        es.input_job_description(status_generator())
        es.input_image_upload()
        es.input_new_add_note(status_generator())
        es.save_all_data_of_job_title()
        if 'Required' in es.job_title_required_validation():
            assert True
            log.info('Test Case Pass')
        else:
            log.critical('Test Case Fail')
            assert False
            
    def test_new_job_title_with_all_input_blank_data(self):
        log = self.getthelogs()
        lg = Login(self.driver)
        db = dashboard_data(self.driver)
        es = jobtitle_data(self.driver)
        log.info('TEST CASE, test_new_job_title_with_all_input_blank_data')
        log.info('Test case starting')
        lg.input_username(config.get("credential", "correct_username"))
        lg.input_password(config.get("credential", "correct_password"))
        lg.click_login()
        db.click_admin()
        time.sleep(2)
        db.click_job()
        db.click_job_title_section()
        es.click_add_new_job_title()
        time.sleep(1)
        es.save_all_data_of_job_title()
        time.sleep(2)
        if 'Required' in es.job_title_required_validation():
            assert True
            log.info('Test Case Pass')
        else:
            log.critical('Test Case Fail')
            assert False
    
    def test_new_job_title_with_exceed_limit_new_job_title(self):
        log = self.getthelogs()
        lg = Login(self.driver)
        db = dashboard_data(self.driver)
        es = jobtitle_data(self.driver)
        log.info('TEST CASE, test_new_job_title_with_all_input_blank_data')
        log.info('Test case starting')
        lg.input_username(config.get("credential", "correct_username"))
        lg.input_password(config.get("credential", "correct_password"))
        lg.click_login()
        db.click_admin()
        time.sleep(2)
        db.click_job()
        db.click_job_title_section()
        es.click_add_new_job_title()
        es.exceed_limit_of_new_job_title()
        es.input_job_description(status_generator())
        es.input_image_upload()
        es.input_new_add_note(status_generator())
        time.sleep(3)
        es.save_all_data_of_job_title()
        time.sleep(2)
        if 'Should not exceed 100 characters' in es.job_title_required_validation():
            assert True
            log.info('Test Case Pass')
        else:
            log.critical('Test Case fail')
            assert False
