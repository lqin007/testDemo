from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from PythonPractice.EnterpriseWechatWeb.page.basePage import BasePage


class ContactPage(BasePage):
    ele_add = (By.CSS_SELECTOR, '.member_colLeft_top_addBtn')
    ele_addDepartment = (By.LINK_TEXT, '添加部门')
    def goto_addDepartmentPage(self):
        sleep(2)
        self.find(self.ele_add).click()
        self.find(self.ele_addDepartment).click()
        from PythonPractice.EnterpriseWechatWeb.page.addDepartmentPage import AddDepartmentPage
        return AddDepartmentPage(self.driver)
    def get_department_list(self):
        #WebDriverWait(self.driver,5000).until(expected_conditions.)
        sleep(3)
        ele_departments = self.finds(
            (By.XPATH,"//a[contains(@class,'jstree-anchor')]"))
        print(ele_departments)
        results = [i.text for i in ele_departments]
        print(results)
        return results
