import pytest
import yaml
import allure



@allure.feature("计算器")
class TestCaculate():
    data = yaml.safe_load(open("./testdata/testyaml"))

    @pytest.mark.parametrize('a,b,result', data['add']['data'], ids=data['add']['name'])
    @allure.story("计算器加法")
    def test_add(self,cal, a, b, result):
        with allure.step("加法计算结果"):
            expect = cal.addition(a, b)
            print(expect)
        with allure.step("加法断言结果"):
            assert expect == result

    @pytest.mark.parametrize('a,b,result', data['sub']['data'], ids=data['sub']['name'])
    @allure.story("计算器减法")
    def test_sub(self, cal, a, b, result):
        with allure.step("减法计算结果"):
            expect = cal.subtraction(a, b)
            print(expect)
        with allure.step("减法断言结果"):
            assert expect == result

    @pytest.mark.parametrize('a,b,result', data['mul']['data'], ids=data['mul']['name'])
    @allure.story("计算器乘法")
    def test_mul(self, cal, a, b, result):
        with allure.step("乘法计算结果"):
            expect = cal.multiplication(a, b)
            print(expect)
        with allure.step("乘法断言结果"):
            assert expect == result

    @pytest.mark.parametrize('a,b,result', data['div']['data'], ids=data['div']['name'])
    @allure.story("计算器除法")
    def test_div(self, cal, a, b, result):
        with allure.step("除法计算结果"):
            expect = cal.division(a, b)
            print(expect)
        with allure.step("除法断言结果"):
            assert expect == result



