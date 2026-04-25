import yaml


# 读取yaml文件
def load_yaml(path):
    file = open(path,'r',encoding='utf-8')
    data = yaml.load(file,Loader=yaml.FullLoader)
    return data




# 测试是否正常读取yaml文件
if __name__ == '__main__':
    load_yaml('../data/userinfo.yaml')
    print(yaml.dump(load_yaml('../data/userinfo.yaml')))