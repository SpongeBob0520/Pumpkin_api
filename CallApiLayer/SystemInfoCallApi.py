from aspect.CallApiAspect import CallApiAspect
from bean.UrlParams import UrlParams
from config import ReadConfigFile
from httpSendRequest import HttpUtils
from logger.logge import logger


class SystemInfoCallApi:

    @CallApiAspect.aroundHandle(CallApiAspect(),
                                servletPath=ReadConfigFile.classNameAndFieldName('systeminfo', 'praiseComentList'),
                                reauestType='GET')
    def praiseComentList(self, urlParams: UrlParams = None):
        logger.info("开始调用" + str(urlParams.url))
        infReturn = HttpUtils.httpGet(urlParams.url, urlParams, params=urlParams.param, headers=urlParams.headMap,
                                      verify=False)
        return infReturn

    @CallApiAspect.aroundHandle(CallApiAspect(),
                                servletPath=ReadConfigFile.classNameAndFieldName('systeminfo', 'remindNavgation'),
                                reauestType='GET')
    def remindNavgation(self, urlParams: UrlParams = None):
        logger.info("开始调用" + str(urlParams.url))
        infReturn = HttpUtils.httpGet(urlParams.url, urlParams, params=urlParams.param, headers=urlParams.headMap,
                                      verify=False)
        return infReturn

    @CallApiAspect.aroundHandle(CallApiAspect(),
                                servletPath=ReadConfigFile.classNameAndFieldName('systeminfo', 'updateNotifyRead'),
                                reauestType='GET')
    def updateNotifyRead(self, urlParams: UrlParams = None):
        logger.info("开始调用" + str(urlParams.url))
        infReturn = HttpUtils.httpGet(urlParams.url, urlParams, params=urlParams.param, headers=urlParams.headMap,
                                      verify=False)
        return infReturn

    @CallApiAspect.aroundHandle(CallApiAspect(),
                                servletPath=ReadConfigFile.classNameAndFieldName('systeminfo', 'updateRemindStatus'),
                                reauestType='GET')
    def updateRemindStatus(self, urlParams: UrlParams = None):
        logger.info("开始调用" + str(urlParams.url))
        infReturn = HttpUtils.httpGet(urlParams.url, urlParams, params=urlParams.param, headers=urlParams.headMap,
                                      verify=False)
        return infReturn

    @CallApiAspect.aroundHandle(CallApiAspect(),
                                servletPath=ReadConfigFile.classNameAndFieldName('systeminfo', 'remindStatus'),
                                reauestType='GET')
    def remindStatus(self, urlParams: UrlParams = None):
        logger.info("开始调用" + str(urlParams.url))
        infReturn = HttpUtils.httpGet(urlParams.url, urlParams, params=urlParams.param, headers=urlParams.headMap,
                                      verify=False)
        return infReturn

    @CallApiAspect.aroundHandle(CallApiAspect(),
                                servletPath=ReadConfigFile.classNameAndFieldName('poster', 'screenRotation'),
                                reauestType='GET')
    def screenRotation(self, urlParams: UrlParams = None):
        logger.info("开始调用: " + str(urlParams.url))
        infReturn = HttpUtils.httpGet(urlParams.url, urlParams, params=urlParams.param, headers=urlParams.headMap,
                                      verify=False)
        return infReturn
