from aspect.CallApiAspect import CallApiAspect
from bean.UrlParams import UrlParams
from config import ReadConfigFile
from httpSendRequest import HttpUtils
from logger.logge import logger


class UserCallApi:

    @CallApiAspect.aroundHandle(CallApiAspect(),
                                servletPath=ReadConfigFile.classNameAndFieldName('user', 'addFeedback'),
                                reauestType='GET')
    def addFeedback(self, urlParams: UrlParams = None):
        logger.info("开始调用" + str(urlParams.url))
        infReturn = HttpUtils.httpPost(urlParams.url, urlParams, data=urlParams.get_param(), headers=urlParams.headMap,verify=False)
        return infReturn

    @CallApiAspect.aroundHandle(CallApiAspect(),
                                servletPath=ReadConfigFile.classNameAndFieldName('user', 'userPraiseStatus'),
                                reauestType='GET')
    def userPraiseStatus(self, urlParams: UrlParams = None):
        logger.info("开始调用" + str(urlParams.url))
        infReturn = HttpUtils.httpGet(urlParams.url, urlParams, params=urlParams.get_param(), headers=urlParams.headMap,verify=False)
        return infReturn

    @CallApiAspect.aroundHandle(CallApiAspect(),
                                servletPath=ReadConfigFile.classNameAndFieldName('user', 'userCollectionStatus'),
                                reauestType='GET')
    def userCollectionStatus(self, urlParams: UrlParams = None):
        logger.info("开始调用" + str(urlParams.url))
        infReturn = HttpUtils.httpGet(urlParams.url, urlParams, params=urlParams.get_param(), headers=urlParams.headMap,verify=False)
        return infReturn

    @CallApiAspect.aroundHandle(CallApiAspect(),
                                servletPath=ReadConfigFile.classNameAndFieldName('user', 'userFanList'),
                                reauestType='GET')
    def userFanList(self, urlParams: UrlParams = None):
        logger.info("开始调用" + str(urlParams.url))
        infReturn = HttpUtils.httpGet(urlParams.url, urlParams, headers=urlParams.headMap,verify=False)
        return infReturn

    @CallApiAspect.aroundHandle(CallApiAspect(),
                                servletPath=ReadConfigFile.classNameAndFieldName('user', 'userSecretConfig'),
                                reauestType='GET')
    def userSecretConfig(self, urlParams: UrlParams = None):
        logger.info("开始调用" + str(urlParams.url))
        infReturn = HttpUtils.httpGet(urlParams.url, urlParams, headers=urlParams.headMap,verify=False)
        return infReturn

    @CallApiAspect.aroundHandle(CallApiAspect(),
                                servletPath=ReadConfigFile.classNameAndFieldName('user', 'followAndCancel'),
                                reauestType='POST')
    def followAndCancel(self, urlParams: UrlParams = None):
        logger.info("开始调用" + str(urlParams.url))
        infReturn = HttpUtils.httpPost(urlParams.url, urlParams, data=urlParams.get_param(), headers=urlParams.headMap,verify=False)
        return infReturn
