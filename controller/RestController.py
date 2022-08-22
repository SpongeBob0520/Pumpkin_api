import os, sys

root_path = os.path.abspath(__file__)
root_path = '/'.join(root_path.split('/')[:-2])
sys.path.append(root_path)


from flask import request
from aspect.ControllerAspect import ControllerAspect
from config import ReadConfigFile, GlobalConfig
from config.FlaskConfig import flask
from dao.DatabaseOperation import DatabaseOperation
from testCase.ActorTestCase import ActorTestCase
from testCase.HallTestCase import HallTestCase
from testCase.HomeTestCase import HomeTestCase
from testCase.MovieTestCase import MovieTestCase
from testCase.QrCodeTestCase import QrCodeTestCase
from testCase.SearchTestCase import SearchTestCase
from testCase.SystemInfoTestCase import SystemInfoTestCase
from testCase.UserTestCase import UserTestCase
from utils import ResponseUtils


@flask.route("/notice", methods=['GET', 'POST'])
@ControllerAspect.listenControllerMethod(ControllerAspect())
def postMethod():
    envPrifx = request.args.get('envPrifx')
    phone = request.args.get('phone')
    # 更新环境数据
    updataEnvInfoConfig(envPrifx, phone)
    # 首页组件资源相关
    case = HomeTestCase()
    case.testHom()
    case.testHomeAssemblyAllResources()
    case.testDoubleRequestCheck()

    # 搜索相关
    searchCase = SearchTestCase()
    searchCase.testSearchKeyWords()
    searchCase.testTvSearchKeyWords()
    searchCase.testSearchHot()
    searchCase.testAskClickSearchMovie()
    searchCase.testConfSearchIcons()
    # movie相关
    movieCase = MovieTestCase()
    movieCase.testMovieSimilerMovie()
    movieCase.testLikeMovie()
    movieCase.testMovieInfoById()
    movieCase.testUserMovieRecord()
    movieCase.testDrmPlayMovieUrl()
    movieCase.testMoreSearchReservation()
    # 影人相关-总和
    actorCase = ActorTestCase()
    actorCase.testActorIdByMovieId()
    # 系统消息
    systemCase = SystemInfoTestCase()
    systemCase.testSystemInfo()
    qrCodeCase = QrCodeTestCase()
    qrCodeCase.testQrCode()
    # 用户信息
    userCase = UserTestCase()
    userCase.testUserSecretConfig()
    userCase.testUserFanList()
    userCase.testUserPraiseStatus()
    userCase.testUserCollectionStatus()
    # 放映厅相关
    hallCase = HallTestCase()
    hallCase.testCreatHall()
    hallCase.testDisMissHall()
    #
    globleReport = GlobalConfig.getReportClassInfo()
    return ResponseUtils.reportToStrModelAndView(globleReport)


# 更新域名
def updataEnvInfoConfig(envPrifx: str = None, phone=None):
    if envPrifx is not None and envPrifx != '':
        # 项目中配置的默认就是beta环境数据，如果不是beta环境就为测试环境将域名改成测试环境，线上环境不能使用，需要特殊配置，如有需要自己改这里的代码
        if envPrifx is not None and 'beat' not in envPrifx:
            headerMap = ReadConfigFile.classNameAndFieldName('header')
            headerMap['envPrifx'] = envPrifx
            headerMap['apiPrifx'] = 'https://dev-environmental.vcinema.cn:8077'
            headerMap['dorasPrifx'] = 'http://dev.doras.vcinema.cn:3100'
            headerMap['secretApiPrifx'] = 'https://dev-environmental.vcinema.cn:1001'
        # 如果传入的手机号码有指定则使用指定的手机号码,没有指定就使用默认的
        if phone is not None and phone != '':
            phone = ReadConfigFile.classNameAndFieldName('phone')
            phone['phone'] = phone


@flask.route("/searchReport", methods=['GET', 'POST'])
def searchReportByMillers():
    millis = request.args.get('millis')
    report = DatabaseOperation().searchReport(millis)
    return ResponseUtils.responseModelAndView(report)


if __name__ =='__main__':
   flask.run(host="127.0.0.1", port=5000, debug='False')

