'''
    关键字的封装
'''
import json

import allure
import jsonpath

import requests

class ApiKeys():
    # def __init__(self):
    #     self.requests = requests.Session()

    # GET请求
    @allure.step("发送get请求")
    def do_get(self,url,data=None,**kwargs):
        return requests.get(url=url,params=data,**kwargs)

    # POST请求
    @allure.step("发送post请求")
    def do_post(self,url,data=None,**kwargs):
        return requests.post(url=url,data=data,**kwargs)


    #PUT请求
    @allure.step("发送put请求")
    def do_put(self,url,data=None,**kwargs):
        return requests.put(url=url,data=data,**kwargs)


    # DELETE请求
    @allure.step("发送delete请求")
    def do_delete(self,url,data=None,**kwargs):
        return requests.delete(url=url,data=data,**kwargs)


    # 获取返回结果字典
    @allure.step("获取返回结果字典")
    def get_api_keys(self,data,key):
        json_data = json.loads(data)
        value = jsonpath.jsonpath(json_data,'$..{0}'.format(key))
        return value[0]