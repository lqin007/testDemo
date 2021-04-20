import yaml
import pytest
from PythonPractice.EnterpriseWechatWeb.page.mainPage import MainPage



class TestAddDepartment:
    test_data_path ="../testdata/department.yml"
    with open(test_data_path,encoding='utf-8') as f:
        test_data = yaml.safe_load(f)

    @pytest.mark.parametrize('departmentName',test_data)
    def test_addDepFromMembert_success(self, conf, departmentName):
        #点击添加成员、添加部门跳转到添加部门页面，添加新的部门,断言
        self.addDepartmentPage = conf.goto_addMemberPage().goto_addDepartmentPage()
        departments_list = self.addDepartmentPage.add_department(departmentName).get_department_list()
        assert departmentName in departments_list

    @pytest.mark.parametrize('departmentName', test_data)
    def test_addDepFromMembert_faile(self, conf, departmentName):
        # 点击添加成员、添加部门跳转到添加部门页面，添加已存在的部门，断言
        self.addDepartmentPage = conf.goto_addMemberPage().goto_addDepartmentPage()
        self.addDepartmentPage.add_department(departmentName)
        assert '该部门已存在' in self.addDepartmentPage.get_tips()
        print("该部门已存在，添加失败")

    def test_addDepFromContact(self,conf):
        conf.goto_contactPage().goto_addDepartmentPage().add_department('一个XX部门')
