'''
    测试用例：只写测试用例，但运行此测试用例文件
'''
import sys

import allure
import pytest

from api_keys.api_keys import ApiKeys
from data_driver import yaml_driver
from params.allParams import LOGIN, URL


# epic是大需求，story是小需求
# @allure.epic("模块需求")
class Apicase():
    # @allure.story("01.登录接口测试")
    def to_login(self, userData):
        ak = ApiKeys()
        url = URL + LOGIN
        userinfo = {
            'type': userData['user']['type'],
            'accounts': userData['user']['accounts'],
            'pwd': userData['user']['pwd']
        }
        res = ak.do_post(url=url,json=userinfo)
        # ！print这一行至关重要，不加执行后stdout中展示响应结果
        print(res.text)
        with allure.step("校验响应结果"):
            msg = ak.get_api_keys(res.text, 'msg')
            # sys.__stdout__.write("【调试】准备打印 msg\n")
            # sys.__stdout__.flush()
            # print(msg)
            # allure.attach(str(msg), name="login_response_msg", attachment_type=allure.attachment_type.TEXT)
            assert msg == userData['msg']


