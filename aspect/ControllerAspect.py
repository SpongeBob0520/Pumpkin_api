from bean.CheckResponseResult import CheckResponseResult
from config import FlaskConfig, GlobalConfig
from dao.DatabaseOperation import DatabaseOperation
from logger.logge import logger
from utils import ResponseUtils
from utils.HtmlTemplate import HtmlTemplate


class ControllerAspect:
    # 监控接口层
    def listenControllerMethod(self):
        def handlerFunc(func):
            def handlerControllerExcept(*args, **kwargs):
                logger.info("正在进行监控")
                t = None
                try:
                    t = func(*args, **kwargs)
                except BaseException() as e:
                    logger.info(e)
                    result = {"result": "执行过程中出现错误,请检查项目"}
                    return ResponseUtils.responseModelAndView(result)
                finally:
                    # 数据库插入
                    # DatabaseOperation().batchInsertDB(GlobalConfig.getReportClassInfo())
                    # 报告生成为html文件
                    # HtmlTemplate().generateHtmlReport(GlobalConfig.getReportClassInfo())
                    # 发送邮件的方法 参考：https://www.cnblogs.com/lovealways/p/6701662.html
                    # 最后重置报告数据
                    GlobalConfig.setRepotClassInfo(CheckResponseResult())
                    # 此处要加上邮件报告
                    logger.info("记得发报告")
                return t
            return handlerControllerExcept
        return handlerFunc
