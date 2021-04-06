import pytest
from caculatePractice.caculate import Caculate

@pytest.fixture(scope='class')
def cal():
    print("计算开始")
    cal = Caculate()
    yield cal
    print("计算结束")
