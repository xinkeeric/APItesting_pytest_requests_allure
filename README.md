pytest+requests+allure 接口自动化测试框架

# 项目目录结构

```
└── pytest+requests+allure
    ├── api_keys
    │   ├── __init__.py
    │   └── api_keys.py #关键字封装
    ├── cases
    │   ├── __init__.py
    │   └── case.py #测试用例封装
    ├── data
    │   ├── __init__.py
    │   └── userinfo.yaml #数据文件
    ├── data_driver
    │   ├── __init__.py
    │   └── yaml_driver.py #数据驱动
    ├── logic
    │   ├── __init__.py
    │   └── test_Login.py #测试用例调用
    ├── params
    │   ├── __init__.py
    │   └── allParams.py #配置
    ├── PROJECT_STRUCTURE.md
    ├── conftest.py 
    ├── main.py #主程序入口
    ├── make_file_tree.py
    └── requirements.txt #依赖
```
