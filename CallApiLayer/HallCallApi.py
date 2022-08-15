from aspect.CallApiAspect import CallApiAspect
from bean.UrlParams import UrlParams
from config import ReadConfigFile
from httpSendRequest import HttpUtils
from logger.logge import logger


class HallCallApi:

    @CallApiAspect.aroundHandle(CallApiAspect(),
                                servletPath=ReadConfigFile.classNameAndFieldName('hall', 'create_channel'),
                                reauestType='POST')
    def ceatHall(self, urlParams: UrlParams = None):
        logger.info("开始调用" + str(urlParams.url))
        infReturn = HttpUtils.httpPost(urlParams.url, urlParams, headers=urlParams.headMap,
                                       verify=False)
        return infReturn

    @CallApiAspect.aroundHandle(CallApiAspect(),
                                servletPath=ReadConfigFile.classNameAndFieldName('hall', 'dismissHall'),
                                reauestType='POST')
    def dismissHall(self, urlParams: UrlParams = None):
        logger.info("开始调用" + str(urlParams.url))
        infReturn = HttpUtils.httpPost(urlParams.url, urlParams, headers=urlParams.headMap,
                                       verify=False)
        return infReturn

    @CallApiAspect.aroundHandle(CallApiAspect(),
                                servletPath=ReadConfigFile.classNameAndFieldName('hall', 'pumkinOnlineHall'),
                                reauestType='GET')
    def pumkinOnlineHall(self, urlParams: UrlParams = None):
        logger.info("开始调用" + str(urlParams.url))
        infReturn = HttpUtils.httpGet(urlParams.url, urlParams, headers=urlParams.headMap,
                                       verify=False)
        return infReturn

    @CallApiAspect.aroundHandle(CallApiAspect(),
                                servletPath=ReadConfigFile.classNameAndFieldName('hall', 'addHall'),
                                reauestType='POST')
    def addHall(self, urlParams: UrlParams = None):
        logger.info("开始调用" + str(urlParams.url))
        infReturn = HttpUtils.httpPost(urlParams.url, urlParams, data=urlParams.get_param(), headers=urlParams.headMap,
                                       verify=False)
        return infReturn

    @CallApiAspect.aroundHandle(CallApiAspect(),
                                servletPath=ReadConfigFile.classNameAndFieldName('hall', 'sendScreenemoji'),
                                reauestType='POST')
    def sendScreenemoji(self, urlParams: UrlParams = None):
        logger.info("开始调用" + str(urlParams.url))
        infReturn = HttpUtils.httpPost(urlParams.url, urlParams, data=urlParams.get_param(), headers=urlParams.headMap,
                                       verify=False)
        return infReturn

    @CallApiAspect.aroundHandle(CallApiAspect(),
                                servletPath=ReadConfigFile.classNameAndFieldName('hall', 'bulletList'),
                                reauestType='GET')
    def bulletList(self, urlParams: UrlParams = None):
        logger.info("开始调用" + str(urlParams.url))
        infReturn = HttpUtils.httpGet(urlParams.url, urlParams, headers=urlParams.headMap,
                                      verify=False)
        return infReturn

    @CallApiAspect.aroundHandle(CallApiAspect(),
                                servletPath=ReadConfigFile.classNameAndFieldName('hall', 'waringHall'),
                                reauestType='GET')
    def waringHall(self, urlParams: UrlParams = None):
        logger.info("开始调用" + str(urlParams.url))
        infReturn = HttpUtils.httpGet(urlParams.url, urlParams, headers=urlParams.headMap,
                                      verify=False)
        return infReturn

    @CallApiAspect.aroundHandle(CallApiAspect(),
                                servletPath=ReadConfigFile.classNameAndFieldName('hall', 'onlineUsersHall'),
                                reauestType='GET')
    def onlineUsersHall(self, urlParams: UrlParams = None):
        logger.info("开始调用" + str(urlParams.url))
        infReturn = HttpUtils.httpGet(urlParams.url, urlParams, headers=urlParams.headMap,
                                      verify=False)
        return infReturn

    @CallApiAspect.aroundHandle(CallApiAspect(),
                                servletPath=ReadConfigFile.classNameAndFieldName('hall', 'channelInfo'),
                                reauestType='GET')
    def channelInfo(self, urlParams: UrlParams = None):
        logger.info("开始调用" + str(urlParams.url))
        infReturn = HttpUtils.httpGet(urlParams.url, urlParams, headers=urlParams.headMap,
                                      verify=False)
        return infReturn

    @CallApiAspect.aroundHandle(CallApiAspect(),
                                servletPath=ReadConfigFile.classNameAndFieldName('hall', 'obtainChannelsAllHall'),
                                reauestType='GET')
    def obtainChannelsAllHall(self, urlParams: UrlParams = None):
        logger.info("开始调用" + str(urlParams.url))
        infReturn = HttpUtils.httpGet(urlParams.url, urlParams, headers=urlParams.headMap,
                                      verify=False)
        return infReturn

    @CallApiAspect.aroundHandle(CallApiAspect(),
                                servletPath=ReadConfigFile.classNameAndFieldName('hall', 'obtainChannelsAllHall_V2'),
                                reauestType='GET')
    def obtainChannelsAllHall_V2(self, urlParams: UrlParams = None):
        logger.info("开始调用" + str(urlParams.url))
        infReturn = HttpUtils.httpGet(urlParams.url, urlParams, headers=urlParams.headMap,
                                      verify=False)
        return infReturn

    @CallApiAspect.aroundHandle(CallApiAspect(),
                                servletPath=ReadConfigFile.classNameAndFieldName('hall', 'obtainChannelsAllHall_V3'),
                                reauestType='GET')
    def obtainChannelsAllHall_V3(self, urlParams: UrlParams = None):
        logger.info("开始调用" + str(urlParams.url))
        infReturn = HttpUtils.httpGet(urlParams.url, urlParams, headers=urlParams.headMap,
                                      verify=False)
        return infReturn

    @CallApiAspect.aroundHandle(CallApiAspect(),
                                servletPath=ReadConfigFile.classNameAndFieldName('hall', 'channelHallHistory'),
                                reauestType='GET')
    def channelHallHistory(self, urlParams: UrlParams = None):
        logger.info("开始调用" + str(urlParams.url))
        infReturn = HttpUtils.httpGet(urlParams.url, urlParams, headers=urlParams.headMap,
                                      verify=False)
        return infReturn

    @CallApiAspect.aroundHandle(CallApiAspect(),
                                servletPath=ReadConfigFile.classNameAndFieldName('hall', 'userRecentHall'),
                                reauestType='GET')
    def userRecentHall(self, urlParams: UrlParams = None):
        logger.info("开始调用" + str(urlParams.url))
        infReturn = HttpUtils.httpGet(urlParams.url, urlParams, headers=urlParams.headMap,
                                      verify=False)
        return infReturn