import pytest
from PythonPractice.EnterpriseWechatWeb.page.mainPage import MainPage

@pytest.fixture(scope='session')
def conf():
    main = MainPage()
    print("添加部门测试开始")
    yield main
    main.end()
    print("添加部门测试结束")