from PythonPractice.EnterpriseWechatWeb.page.addMemberPage import AddMemberPage
from PythonPractice.EnterpriseWechatWeb.page.basePage import BasePage
from selenium.webdriver.common.by import By
from PythonPractice.EnterpriseWechatWeb.page.contactPage import ContactPage

class MainPage(BasePage):
    base_url = "https://work.weixin.qq.com/wework_admin/frame#index"
    #定义元素类变量，ele_addMember“添加成员”按钮，ele_contact“通讯录“按钮
    ele_addMember = (By.XPATH,'//*[@id="_hmt_click"]/div[1]/div[4]/div[2]/a[1]/div/span[2]')
    ele_contact = (By.XPATH,'//*[@id="menu_contacts"]/span')
    def goto_addMemberPage(self):
        self.driver.get(self.base_url)
        self.find(self.ele_addMember).click()
        return AddMemberPage(self.driver)
    def goto_contactPage(self):
        self.driver.get(self.base_url)
        self.find(self.ele_contact).click()
        return ContactPage(self.driver)
