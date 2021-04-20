from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class BasePage:
    #子类不重写 __init__，实例化子类时，会自动调用父类定义的 __init__构造方法，参数设置默认值base_driver=None
    def __init__(self,base_driver=None):
        if base_driver is None:
            #base_url,定义打开主页面
            #base_url = "https://work.weixin.qq.com/wework_admin/frame#index"
            #浏览器复用模式
            chrome_arg = Options()
            chrome_arg.debugger_address = "127.0.0.1:9222"
            self.driver = webdriver.Chrome(options=chrome_arg)
            #self.driver.get(base_url)
            #设置隐式等待
            self.driver.implicitly_wait(5)
        elif base_driver is not None:
            #实例化driver后，后续传递该driver，无需重复实例化
            self.driver = base_driver
    #封装元素查找方法，便于切换技术栈时代码的可维护性
    #使用解元祖操作
    def find(self,locator):
        return self.driver.find_element(*locator)
    def finds(self,locator):
        return self.driver.find_elements(*locator)
    def end(self):
        self.driver.quit()
