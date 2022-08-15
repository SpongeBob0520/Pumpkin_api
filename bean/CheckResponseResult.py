class CheckResponseResult:
    def __init__(self):
        self.id = None
        # 标记当前的执行地点
        self.flag = None
        # 总执行用例数量
        self.totalCase = None
        # 执行的方法名称 - 记录对外开放运行的方法名 有条件可以翻译成用例名称
        self.methodName = None
        # 方法执行前的描述
        # 如：xxxx接口校验开始执行 --可用可不用
        self.msg = None
        # 接口测试结果 --总结果
        self.result = True
        # 拓展字段 - 备用
        # 作为执行时间使用了
        self.expand = None
        # 时间戳 - 用来做与执行集合做关联
        self.millis = None
        # 存放接口列表
        self.infCallSequence = []

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_flag(self):
        return self.flag

    def set_flag(self, flag):
        self.flag = flag

    def get_totalCase(self):
        return self.totalCase

    def set_totalCase(self, totalCase):
        self.totalCase = totalCase

    def get_methodName(self):
        return self.methodName

    def set_methodName(self, methodName):
        self.methodName = methodName

    def get_msg(self):
        return self.msg

    def set_msg(self, msg):
        self.msg = msg

    def get_result(self):
        return self.result

    def set_result(self, result):
        self.result = result

    def get_expand(self):
        return self.expand

    def set_expand(self, expand):
        self.expand = expand

    def get_millis(self):
        return self.millis

    def set_millis(self, millis):
        self.millis = millis

    def get_infCallSequence(self):
        return self.infCallSequence

    def set_infCallSequence(self, infCallSequence):
        self.infCallSequence = infCallSequence


# 快速生成get和set方法
if __name__ == '__main__':
    a = CheckResponseResult()
    for i in a.__dict__:
        print("def get_" + str(i) + "(self):")
        print("    return self." + str(i))
        print("\n")
        print("def set_" + str(i) + "(self, " + str(i) + "):")
        print("    self." + str(i) + " = " + str(i))
        print("\n")

