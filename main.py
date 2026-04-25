'''
    主程序入口 用来执行测试用例及生成报告
'''
import os

import pytest


def run():
    print("当前工作目录:", os.getcwd())
    print("目录下的内容:", os.listdir('.'))
    # pytest.main(['-v', './cases/test_case.py',
    #              '--alluredir', './result', '--clean-alluredir'])
    pytest.main(['-v', './logic/test_Login.py',
                 '--alluredir', './result', '--clean-alluredir'])
    # pytest.main(['-v','./test_cases/test_case.py',])

    os.system('allure serve result')
    # 生成html文件
    # os.system('allure generate ./result/ -o ./report_allure/ --clean')

if __name__ == '__main__':
    run()