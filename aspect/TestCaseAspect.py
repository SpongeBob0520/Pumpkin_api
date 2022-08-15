from config import GlobalConfig
from logger.logge import logger


class TestCaseAspect:

    def testCaseListen(func):
        def testCaseHandler(*args, **kwargs):
            logger.info("当前运行的方法："+str(func.__name__))
            globleReport = GlobalConfig.getReportClassInfo()
            # 获取方法名
            funName = func.__name__
            try:
                func(*args, **kwargs)
                # 获取全局参数中的接口集合
                sequence = globleReport.get_infCallSequence()
                for value in sequence:
                    if value.testCaseName is None:
                        # 这里是默认将用例层的方法直接放入报告中，可以再建一个配置文件将用例层的方法名和配置文件中的对应起来翻译成中文
                        value.testCaseName = funName
            except BaseException as e:
                logger.info("发生错误："+str(e))
                response = GlobalConfig.getInterResponse()
                # 如果发生了异常说明执行过程中出现了异常，需要进行记录
                # 总报告设置成False
                globleReport.set_result(False)
                sequence = globleReport.get_infCallSequence()
                if sequence is not None:
                    # 将接口信息列表翻转一下
                    sequence.reverse()
                    for interInf in sequence:
                        # 已存储的接口信息
                        interface_name = interInf.get_interfaceName()
                        if str(response.url).find(str(interface_name)) > -1:
                            interInf.set_infEnd(False)
                            interInf.errorMsg = str(e)
                            if interInf.testCaseName is None:
                                # 这里是默认将用例层的方法直接放入报告中，可以再建一个配置文件将用例层的方法名和配置文件中的对应起来翻译成中文
                                interInf.testCaseName = funName
                            # 翻转回去避免数据错乱
                            sequence.reverse()
                            break
                # return func(*args, **kwargs)
            # return func(*args, **kwargs)
        return testCaseHandler


