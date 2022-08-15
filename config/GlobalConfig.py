# 设置Token
import copy
import time
from requests import Response
from bean.CheckResponseResult import CheckResponseResult


def setGlobalPumkinUserId(id=None):
    global userId
    userId = id


# 设置用户id的值
def getGlobalPumkinUserId():
    if 'userId' not in globals():
        setGlobalPumkinUserId('4017434')
    return userId


def setGlobalPumPkinToken(pumPkinTokenParam=None):
    global pumPkinToken
    pumPkinToken = pumPkinTokenParam


# 存储Token
def getGlobalPumPkinToken():
    if 'pumPkinToken' not in globals():
        setGlobalPumPkinToken(None)
    return pumPkinToken


# 设置签名信息
def setGlobalPumPkinTokenInfoMap(pumPkinToken):
    global headerMapTokenInfo
    headerMapTokenInfo = pumPkinToken


# 获取Token签名等相关信息
def getGlobalPumPkinTokenInfoMap():
    if 'headerMapTokenInfo' not in globals():
        setGlobalPumPkinToken(None)
    return headerMapTokenInfo


# 设置报告基础类
def setRepotClassInfo(report: CheckResponseResult = None):
    global checkResponseResult, checkResponseResultCopy
    checkResponseResult = report
    checkResponseResultCopy = copy.copy(checkResponseResult)


# 获取报告基础类信息
def getReportClassInfo():
    # 不存在时要新建创立报告类
    if "checkResponseResult" not in globals():
        millis = time.time()
        result = CheckResponseResult()
        # 设置为毫秒级别的时间戳
        result.set_millis(int(round(millis * 1000)))
        setRepotClassInfo(result)
    # 如果报告存在于全局变量参数中则要判断时间戳是否为空，为应对项目活跃期间有多次请求的情况所以要加上判断
    if "checkResponseResult" in globals():
        getReport = globals().get('checkResponseResult')
        if getReport.millis is None:
            getReport.millis = int(round(time.time() * 1000))
    return checkResponseResult


def getReportClassInfoCopy():
    return checkResponseResultCopy


# 接口返回结果响应信息存储
def setInterResponse(response: Response = None):
    global interfaceResponse
    interfaceResponse = response


# 获取接口返回结果响应信息
def getInterResponse():
    if "interfaceResponse" not in globals():
        setInterResponse(None)
    return interfaceResponse


# 设置递归终止判断标识
def setBecursionFlag(flagResult):
    global flag
    flag = flagResult


# 获取递归终止判断标识
def getBecursionFlag():
    if 'flag' not in globals():
        setBecursionFlag(True)
    return flag


# 设置递归的值
def setResultJson(target):
    global targetValue
    targetValue = target


# 获取递归的值
def getResultJson():
    if 'targetValue' not in globals():
        setResultJson(None)
    return targetValue
