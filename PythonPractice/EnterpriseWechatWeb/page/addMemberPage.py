from time import sleep
from selenium.webdriver.common.by import By
from PythonPractice.EnterpriseWechatWeb.page.addDepartmentPage import AddDepartmentPage
from PythonPractice.EnterpriseWechatWeb.page.basePage import BasePage

class AddMemberPage(BasePage):
    #ele_add“+”控件，ele_addDepartment“添加部门”按钮
    ele_add = (By.CSS_SELECTOR, '.member_colLeft_top_addBtn')
    ele_addDepartment = (By.LINK_TEXT, '添加部门')
    def goto_addDepartmentPage(self):
        sleep(2)
        self.find(self.ele_add).click()
        self.find(self.ele_addDepartment).click()
        return AddDepartmentPage(self.driver)
