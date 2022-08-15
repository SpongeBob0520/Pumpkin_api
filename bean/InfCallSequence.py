class InfCallSequence:
    def __init__(self):
        self.id = None
        self.guanlian = None
        # 用例名称 --该用例下的所有接口统一用这个字段描述
        self.testCaseName = None
        # 接口名称
        self.interfaceName = None
        # 接口请求头
        self.infRequestHeader = None
        # 接口请求参数
        self.infRequestParam = None
        # xxx接口开始执行
        self.infStart = None
        # xxx接口校验结果
        self.infEnd = True
        # 接口返回的结果
        self.infReturnMsg = None
        # 时间戳 - 用来做与总报告做关联
        self.millis = None
        # 错误信息
        self.errorMsg = None

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_guanlian(self):
        return self.guanlian

    def set_guanlian(self, guanlian):
        self.guanlian = guanlian

    def get_testCaseName(self):
        return self.testCaseName

    def set_testCaseName(self, testCaseName):
        self.testCaseName = testCaseName

    def get_interfaceName(self):
        return self.interfaceName

    def set_interfaceName(self, interfaceName):
        self.interfaceName = interfaceName

    def get_infRequestHeader(self):
        return self.infRequestHeader

    def set_infRequestHeader(self, infRequestHeader):
        self.infRequestHeader = infRequestHeader

    def get_infRequestParam(self):
        return self.infRequestParam

    def set_infRequestParam(self, infRequestParam):
        self.infRequestParam = infRequestParam

    def get_infStart(self):
        return self.infStart

    def set_infStart(self, infStart):
        self.infStart = infStart

    def get_infEnd(self):
        return self.infEnd

    def set_infEnd(self, infEnd):
        self.infEnd = infEnd

    def get_infReturnMsg(self):
        return self.infReturnMsg

    def set_infReturnMsg(self, infReturnMsg):
        self.infReturnMsg = infReturnMsg

    def get_millis(self):
        return self.millis

    def set_millis(self, millis):
        self.millis = millis

    def get_errorMsg(self):
        return self.errorMsg

    def set_errorMsg(self, errorMsg):
        self.errorMsg = errorMsg


# 快速生成get和set方法
if __name__ == '__main__':
    a = InfCallSequence()
    for i in a.__dict__:
        print("def get_" + str(i) + "(self):")
        print("    return self." + str(i))
        print("\n")
        print("def set_" + str(i) + "(self, " + str(i) + "):")
        print("    self." + str(i) + " = " + str(i))
        print("\n")
