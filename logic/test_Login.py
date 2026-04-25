'''
    尽量简化用例内容，方便管理用例，以及进行模块划分
'''
import allure
import pytest

from api_keys.api_keys import ApiKeys
from cases.case import Apicase
from data_driver import yaml_driver

@allure.epic('模块')
class TestLogin():

    apicase = Apicase()

    @allure.story("01.登录接口测试")
    @pytest.mark.parametrize('userData', yaml_driver.load_yaml('./data/userinfo.yaml'),
                             ids=["输入正确账号，密码，登录成功"])
    def test_Login(self,userData):
        self.apicase.to_login(userData)
