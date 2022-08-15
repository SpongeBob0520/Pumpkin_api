
from bean.InfCallSequence import InfCallSequence
from config import GlobalConfig
from logger.logge import logger


class HttpAspect:
    def httpListen(func):
        def testHttpHandler(*args, **kwargs):
            global t
            try:
                t = func(*args, **kwargs)
            except Exception() as e:
                logger.info(str(e))
            finally:
                urlParams = args[1]
                # 获取全局变量中的接口返回信息
                response = GlobalConfig.getInterResponse()
                # 获取报告类
                reportInfo = GlobalConfig.getReportClassInfo()
                # 创建接口记录类
                infCall = InfCallSequence()
                infCall.set_infReturnMsg(str(response.content.decode('utf8')))
                infCall.set_interfaceName(urlParams.url)
                infCall.set_infRequestHeader(str(urlParams.headMap))
                infCall.set_infRequestParam(str(urlParams.get_param()))
                # 设置时间戳
                infCall.set_millis(reportInfo.get_millis())

                sequence = reportInfo.get_infCallSequence()
                if sequence is None:
                    sequence = []
                sequence.append(infCall)
            return t
        return testHttpHandler
