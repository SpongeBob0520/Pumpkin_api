# -*-coding:utf-8-*-
import json

import pymysql

from bean.CheckResponseResult import CheckResponseResult
from config import ReadConfigFile
from logger.logge import logger


class DatabaseOperation:

    # 初始化数据 --这里有缺点每次调用都要链接和断开读取文档
    def __init__(self):
        self.connect = pymysql.connect(host=ReadConfigFile.classNameAndFieldName("mysqlConfig", "host"),
                                       user=ReadConfigFile.classNameAndFieldName("mysqlConfig", "username"),
                                       password=ReadConfigFile.classNameAndFieldName("mysqlConfig", "passwrod"),
                                       database=ReadConfigFile.classNameAndFieldName("mysqlConfig", "database"),
                                       charset='utf8', cursorclass=pymysql.cursors.DictCursor)
        self.cursors = self.connect.cursor()

    """批量插入运行结果,进入数据库"""

    def batchInsertDB(self, checkResponseResult: CheckResponseResult):
        try:
            # 主报告的数据准备插入
            paramList = [checkResponseResult.get_methodName(), checkResponseResult.get_msg(),
                         checkResponseResult.get_result(), checkResponseResult.get_expand(),
                         checkResponseResult.get_millis()]
            sequence = checkResponseResult.get_infCallSequence()
            print(checkResponseResult, paramList, sequence)
            sql = 'insert into check_response_result (methodName,msg,result,expand,millis) values (%s,%s,%s,%s,%s)'
            self.cursors.execute(sql, paramList)
            self.connect.commit()
            # 副结果报告数据准备插入
            deputyReportList = []
            for interInf in sequence:
                par = (interInf.interfaceName, interInf.infRequestHeader, interInf.infRequestParam, interInf.infStart,
                       interInf.infEnd, interInf.infReturnMsg, interInf.millis, interInf.errorMsg,
                       interInf.testCaseName)
                deputyReportList.append(par)
            sql = 'insert into inf_call_sequence (interface_name,inf_request_header,inf_request_param,inf_start,inf_end,inf_return_msg,millis,error_msg,test_case_name) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            self.cursors.executemany(sql, deputyReportList)
            self.connect.commit()
        except Exception as e:
            logger.info("报告批量插入时发生错误，请检查：" + str(e))
        finally:
            self.cursors.close()
            self.connect.close()

    # 通过指定的时间戳来获取报告生成的数据
    def searchReport(self, millis: str) -> json:
        fetchall = None
        try:
            print(millis)
            # 查询主报告
            sql = 'SELECT * FROM check_response_result WHERE millis=%s'
            self.cursors.execute(sql, millis)
            self.connect.commit()
            fetchall = self.cursors.fetchall()[0]
            # 查询副报告
            sql = 'SELECT * from inf_call_sequence WHERE millis=%s'
            self.cursors.execute(sql, millis)
            self.connect.commit()
            cursors_fetchall = self.cursors.fetchall()
            # 将副报告插入主报告中
            fetchall['resultInfList'] = cursors_fetchall
        except Exception as e:
            logger.info("查询报告数据出现错误,请检查："+str(e))
        finally:
            self.cursors.close()
            self.connect.close()
        return fetchall


if __name__ == '__main__':

    operation = DatabaseOperation()
    operation.searchReport("1642074778840")
