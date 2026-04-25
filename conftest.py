import allure
import pytest

from api_keys.api_keys import ApiKeys


def pytest_collection_modifyitems(items):
    '''

        测试用例收集完成时，将收集到的item的name和nodeid的中文显示在控制台
        需要跟main函数在一个目录下才生效
    '''
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item._nodeid.encode('utf-8').decode('unicode-escape')

# 获取token 如果只需要这一次 那么需要封装集成在这
# @pytest.fixture(scope='session')
# def token_fix():
#     ak = ApiKeys()
#     with allure.step("发送登录接口请求，并生成token，整个项目仅生成一次"):
#         url = 'http://shop-xo.hctestedu.com/index.php?s=api/user/login&application=app'
#         userinfo = {
#             'type': 'username',
#             'accounts': 'eric_test',
#             'pwd': '123456'
#         }
#         res = ak.to_post(url=url, json=userinfo)
#         token = ak.get_text(res.text, 'token')
#         return ak, token, res