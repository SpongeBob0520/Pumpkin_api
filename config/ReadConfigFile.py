import re
from bean.Application import Application
from config.ConfigParserUtils import ConfigParserUtils
from config.JarProjectUtil import JarProjectUtil
from logger.logge import logger


def setGlobalMethodContext():
    global classNames
    classNames = {}


# 方法级别的存储，目前暂未使用 --也没有完善完全
def getGlobalMethodContext():
    if 'classNames' not in globals():
        global classNames
        classNames = ReadConfigFile().congfiFileIni()
    return classNames


class ReadConfigFile:

    # 一次性将所有的配置文件内容全部读取出来，封装成了:{key:{vakue}}
    def congfiFileIni(self):
        # 传入项目名称,通过项目名称获取该项目下的所有配置文件
        path = JarProjectUtil.project_root_path()
        fileConfig = JarProjectUtil().file_name(path)
        # 返回的值包含了配置文件路径和python文件路径
        # 存储类名
        setGlobalMethodContext()
        # print(classNames)
        global classNames
        # 存储类名下的属性值
        classFiledValue = {}
        for key in fileConfig:
            # 该类为覆盖了父类中默认全部小写的方法
            cp = ConfigParserUtils()
            fileopen = open(key, 'r+')
            cp.read_file(fileopen)
            sections = cp.sections()
            # 这里需要针对 传入的className进行特殊处理 驼峰或者其他的命名规则可以在这里写上
            # 获取最外层的大标识
            for key in sections:
                # 当传进来的className和配置文件中的一致时将返回配置文件中所有相关的配置
                options = cp.options(key)
                # 获取 key = value的key
                for innerKey in options:
                    result = cp.get(key, innerKey)
                    # 如果出现很多类使用时出现字段赋值错误的情况可以加上 类名_属性名 的方式进行区别
                    classFiledValue[innerKey] = result
                classNames[key] = classFiledValue
                classFiledValue = {}
        return classNames


# 提供给外部获取封装完毕后的数据，通过双层key和字段名精确获取
def classNameAndFieldName(className=None, fieldName=None):
    context = getGlobalMethodContext()
    if fieldName is None:
        return context[className]
    class_name = context[className]
    return class_name[fieldName]


# 用来改变全局变量中的值 --一般不用 留空
def replaceConfigData(className=None, fieldName=None, nodeValue=None):
    context = getGlobalMethodContext()
    if fieldName is None:
        context[className] = nodeValue
    context[className][fieldName] = nodeValue


if __name__ == '__main__':
    name = classNameAndFieldName('search', 'hot')
    print(name)
    # ini = ReadConfigFile().congfiFileIni()
    # file_ini = ini.get('Home')
    # for key in ini:
    #     print(key)
    #     get = ini.get(key)
    #     print(get)
