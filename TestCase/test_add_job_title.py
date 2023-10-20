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
        login = Login(self.driver)
        dashboard = dashboard_data(self.driver)
        employeement_status = jobtitle_data(self.driver)
        log.info('TEST CASE, test_new_job_title_with_correct_input_data')
        log.info('Test case starting')
        login.input_username(config.get("credential", "correct_username"))
        login.input_password(config.get("credential", "correct_password"))
        login.click_login()
        dashboard.click_admin()
        time.sleep(2)
        dashboard.click_job()
        dashboard.click_job_title_section()
        old_job_title = 0
        for i in employeement_status.total_job_title_data():
            old_job_title = old_job_title + 1   
        employeement_status.click_add_new_job_title()
        employeement_status.input_new_job_title_role(status_generator())
        employeement_status.input_job_description(status_generator())
        employeement_status.input_image_upload()
        employeement_status.input_new_add_note(status_generator())
        time.sleep(3)
        employeement_status.save_all_data_of_job_title()
        time.sleep(4)
        new_job_title = 0
        for j in employeement_status.total_job_title_data():
            new_job_title = new_job_title + 1
        if old_job_title + 1 == new_job_title:
            assert True
            log.info('Test Case Pass')
        else:
            log.critical('Test Case Fail')
            assert False
        
    def test_new_job_title_with_fill_only_job_title_role_another_field_blank_input(self):
        log = self.getthelogs()
        login = Login(self.driver)
        dashboard = dashboard_data(self.driver)
        employeement_status = jobtitle_data(self.driver)
        log.info('TEST CASE, test_new_job_title_with_fill_only_job_title_role_another_field_blank_input')
        log.info('Test case starting')
        login.input_username(config.get("credential", "correct_username"))
        login.input_password(config.get("credential", "correct_password"))
        login.click_login()
        dashboard.click_admin()
        time.sleep(2)
        dashboard.click_job()
        dashboard.click_job_title_section()
        old_job_title = 0
        for i in employeement_status.total_job_title_data():
            old_job_title = old_job_title + 1
        employeement_status.click_add_new_job_title()
        employeement_status.input_new_job_title_role(status_generator())
        employeement_status.save_all_data_of_job_title()
        new_job_title = 0
        for j in employeement_status.total_job_title_data():
            new_job_title = new_job_title + 1
        if old_job_title + 1 == new_job_title:
            assert True
            log.info('Test Case Pass')
        else:
            log.critical('Test Case Fail')
            assert False

    def test_new_job_title_with_blank_job_title_role_another_field_input_filled(self):
        log = self.getthelogs()
        login = Login(self.driver)
        dashboard = dashboard_data(self.driver)
        employeement_status = jobtitle_data(self.driver)
        log.info('TEST CASE, test_new_job_title_with_fill_only_job_title_role_another_field_blank_input')
        log.info('Test case starting')
        login.input_username(config.get("credential", "correct_username"))
        login.input_password(config.get("credential", "correct_password"))
        login.click_login()
        dashboard.click_admin()
        time.sleep(2)
        dashboard.click_job()
        dashboard.click_job_title_section()
        employeement_status.click_add_new_job_title()
        employeement_status.input_job_description(status_generator())
        employeement_status.input_image_upload()
        employeement_status.input_new_add_note(status_generator())
        employeement_status.save_all_data_of_job_title()
        if 'Required' in employeement_status.job_title_required_validation():
            assert True
            log.info('Test Case Pass')
        else:
            log.critical('Test Case Fail')
            assert False
            
    def test_new_job_title_with_all_input_blank_data(self):
        log = self.getthelogs()
        login = Login(self.driver)
        dashboard = dashboard_data(self.driver)
        employeement_status = jobtitle_data(self.driver)
        log.info('TEST CASE, test_new_job_title_with_all_input_blank_data')
        log.info('Test case starting')
        login.input_username(config.get("credential", "correct_username"))
        login.input_password(config.get("credential", "correct_password"))
        login.click_login()
        dashboard.click_admin()
        time.sleep(2)
        dashboard.click_job()
        dashboard.click_job_title_section()
        employeement_status.click_add_new_job_title()
        time.sleep(1)
        employeement_status.save_all_data_of_job_title()
        time.sleep(2)
        if 'Required' in employeement_status.job_title_required_validation():
            assert True
            log.info('Test Case Pass')
        else:
            log.critical('Test Case Fail')
            assert False
    
    def test_new_job_title_with_exceed_limit_new_job_title(self):
        log = self.getthelogs()
        login = Login(self.driver)
        dashboard = dashboard_data(self.driver)
        employeement_status = jobtitle_data(self.driver)
        log.info('TEST CASE, test_new_job_title_with_all_input_blank_data')
        log.info('Test case starting')
        login.input_username(config.get("credential", "correct_username"))
        login.input_password(config.get("credential", "correct_password"))
        login.click_login()
        dashboard.click_admin()
        time.sleep(2)
        dashboard.click_job()
        dashboard.click_job_title_section()
        employeement_status.click_add_new_job_title()
        employeement_status.exceed_limit_of_new_job_title()
        employeement_status.input_job_description(status_generator())
        employeement_status.input_image_upload()
        employeement_status.input_new_add_note(status_generator())
        time.sleep(3)
        employeement_status.save_all_data_of_job_title()
        time.sleep(2)
        if 'Should not exceed 100 characters' in employeement_status.job_title_required_validation():
            assert True
            log.info('Test Case Pass')
        else:
            log.critical('Test Case fail')
            assert False

    def test_new_job_title_with_exceed_limit_of_all_input_field(self):
        log = self.getthelogs()
        login = Login(self.driver)
        dashboard = dashboard_data(self.driver)
        employeement_status = jobtitle_data(self.driver)
        log.info('TEST CASE, test_new_job_title_with_exceed_limit_of_all_input_field')
        log.info('Test case starting')
        login.input_username(config.get("credential", "correct_username"))
        login.input_password(config.get("credential", "correct_password"))
        login.click_login()
        dashboard.click_admin()
        time.sleep(2)
        dashboard.click_job()
        dashboard.click_job_title_section()
        employeement_status.click_add_new_job_title()
        employeement_status.exceed_limit_of_new_job_title()
        employeement_status.exceed_limit_for_job_description()
        employeement_status.exceed_limit_for_note()
        time.sleep(3)
        if 'Should not exceed 100 characters' in employeement_status.job_title_required_validation() and 'Should not exceed 400 characters' in employeement_status.job_description_required_validation() and 'Should not exceed 400 characters' in employeement_status.job_note_required_validation():
            log.info('Test Case Pass')
            assert True
        else:
            log.critical('Test Case Fail')
            assert False
            
    def test_new_job_title_with_cancel_button_click(self):
        log = self.getthelogs()
        login = Login(self.driver)
        dashboard = dashboard_data(self.driver)
        employeement_status = jobtitle_data(self.driver)
        log.info('TEST CASE, test_new_job_title_with_cancel_button_click')
        log.info('Test case starting')
        login.input_username(config.get("credential", "correct_username"))
        login.input_password(config.get("credential", "correct_password"))
        login.click_login()
        dashboard.click_admin()
        time.sleep(2)
        dashboard.click_job()
        dashboard.click_job_title_section()
        old_job_title = 0
        for i in employeement_status.total_job_title_data():
            old_job_title = old_job_title + 1
        employeement_status.click_add_new_job_title()
        time.sleep(3)
        employeement_status.click_on_cancel_button()
        time.sleep(3)
        new_job_title = 0
        for i in employeement_status.total_job_title_data():
            new_job_title = new_job_title + 1
        if old_job_title == new_job_title:
            assert True
            log.info('Test Case Pass')
        else:
            log.critical('Test Case Fail')
            assert False
            
    def test_delete_job_title(self):
        log = self.getthelogs()
        login = Login(self.driver)
        dashboard = dashboard_data(self.driver)
        employeement_status = jobtitle_data(self.driver)
        log.info('TEST CASE, test_delete_job_title')
        log.info('Test case starting')
        login.input_username(config.get("credential", "correct_username"))
        login.input_password(config.get("credential", "correct_password"))
        login.click_login()
        dashboard.click_admin()
        time.sleep(2)
        dashboard.click_job()
        dashboard.click_job_title_section()
        old_job_title = 0
        for i in employeement_status.total_job_title_data():
            old_job_title = old_job_title + 1
        employeement_status.click_delete_job_title_button()
        time.sleep(2)
        employeement_status.click_confirmation_box_button_yes()
        time.sleep(3)
        new_job_title = 0
        for j in employeement_status.total_job_title_data():
            new_job_title = new_job_title + 1
        if old_job_title - 1 == new_job_title:
            assert True
            log.info('Test Case Pass')
        else:
            log.critical('Test Case Fail')
            assert False
