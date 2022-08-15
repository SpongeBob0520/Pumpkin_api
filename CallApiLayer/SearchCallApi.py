from aspect.CallApiAspect import CallApiAspect
from bean.UrlParams import UrlParams
from config import ReadConfigFile
from httpSendRequest import HttpUtils
from logger.logge import logger


class SearchCallApi:

    @CallApiAspect.aroundHandle(CallApiAspect(), servletPath=ReadConfigFile.classNameAndFieldName('search', 'hot'),
                                reauestType='GET')
    def searchHot(self, urlParams: UrlParams = None):
        logger.info("开始调用" + str(urlParams.url))
        infReturn = HttpUtils.httpGet(urlParams.url, urlParams,headers=urlParams.headMap)
        return infReturn

    @CallApiAspect.aroundHandle(CallApiAspect(), servletPath=ReadConfigFile.classNameAndFieldName('search', 'searchKeyWords'),
                                reauestType='GET')
    def searchKeyWord(self,urlParams: UrlParams = None):
        logger.info("开始调用" + str(urlParams.url))
        infReturn = HttpUtils.httpPost(urlParams.url, urlParams, params=urlParams.get_param(),headers=urlParams.headMap)
        return infReturn

    @CallApiAspect.aroundHandle(CallApiAspect(),
                                servletPath=ReadConfigFile.classNameAndFieldName('search', 'searchFiltrateTv'),
                                reauestType='POST')
    def searchTvKeyWord(self, urlParams: UrlParams = None):
        logger.info("开始调用" + str(urlParams.url))
        infReturn = HttpUtils.httpPost(urlParams.url, urlParams,data=urlParams.get_param(), headers=urlParams.headMap)
        return infReturn

    @CallApiAspect.aroundHandle(CallApiAspect(),
                                servletPath=ReadConfigFile.classNameAndFieldName('search', 'askClickSearchMovie'),
                                reauestType='GET')
    def askClickSearchMovie(self, urlParams: UrlParams = None):
        logger.info("开始调用" + str(urlParams.url))
        infReturn = HttpUtils.httpGet(urlParams.url, urlParams, params=urlParams.get_param(), headers=urlParams.headMap)
        return infReturn

    @CallApiAspect.aroundHandle(CallApiAspect(),servletPath=ReadConfigFile.classNameAndFieldName('search', 'confSearchIcons'),
                                reauestType='GET')
    def confSearchIcons(self, urlParams: UrlParams = None):
        logger.info("开始调用" + str(urlParams.url))
        infReturn = HttpUtils.httpGet(urlParams.url, urlParams,headers=urlParams.headMap)
        return infReturn