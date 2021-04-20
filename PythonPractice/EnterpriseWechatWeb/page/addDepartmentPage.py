from selenium.webdriver.common.by import By
from PythonPractice.EnterpriseWechatWeb.page.basePage import BasePage
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class AddDepartmentPage(BasePage):
    ele_nameInput = (By.NAME, 'name')
    ele_belongToDepartmentSelector = (By.CSS_SELECTOR, '.js_parent_party_name')
    #界面id元素不唯一，使用组合定位方法进行定位
    ele_belongToDepartment = (By.CSS_SELECTOR,".qui_dialog_body.ww_dialog_body [id='1688852014158331_anchor']")
    ele_confirm = (By.LINK_TEXT, '确定')
    def add_department(self,departmentName):
        self.find(self.ele_nameInput).send_keys(departmentName)
        self.find(self.ele_belongToDepartmentSelector).click()
        self.find(self.ele_belongToDepartment).click()
        self.find(self.ele_confirm).click()
        from PythonPractice.EnterpriseWechatWeb.page.contactPage import ContactPage
        return ContactPage(self.driver)
    def get_tips(self):
        ele_exist_tips = (By.ID, 'js_tips')
        WebDriverWait(self.driver, 5000).until(expected_conditions.visibility_of_element_located(ele_exist_tips))
        exist_tips = self.find(ele_exist_tips).text
        return exist_tips