from aspect.CallApiAspect import CallApiAspect
from bean.UrlParams import UrlParams
from config import ReadConfigFile
from httpSendRequest import HttpUtils
from logger.logge import logger


class ActorCallApi:
    @CallApiAspect.aroundHandle(CallApiAspect(), servletPath=ReadConfigFile.classNameAndFieldName('actor', 'actorFilm'), reauestType='GET')
    def actorFilm(self, urlParams: UrlParams = None):
        logger.info("开始调用" + str(urlParams.url))
        infReturn = HttpUtils.httpGet(urlParams.url, urlParams, params=urlParams.get_param(), headers=urlParams.headMap, verify=False)
        return infReturn

    @CallApiAspect.aroundHandle(CallApiAspect(), servletPath=ReadConfigFile.classNameAndFieldName('actor', 'actorListByMovieId'), reauestType='GET')
    def actorListByMovieId(self,urlParams: UrlParams = None):
        logger.info("开始调用" + str(urlParams.url))
        infReturn = HttpUtils.httpGet(urlParams.url, urlParams, params=urlParams.get_param(), headers=urlParams.headMap, verify=False)
        return infReturn

    @CallApiAspect.aroundHandle(CallApiAspect(),
                                servletPath=ReadConfigFile.classNameAndFieldName('actor', 'relatedActorById'),
                                reauestType='GET')
    def relatedActorById(self, urlParams: UrlParams = None):
        logger.info("开始调用" + str(urlParams.url))
        infReturn = HttpUtils.httpGet(urlParams.url, urlParams, params=urlParams.get_param(), headers=urlParams.headMap, verify=False)
        return infReturn

    @CallApiAspect.aroundHandle(CallApiAspect(),
                                servletPath=ReadConfigFile.classNameAndFieldName('actor', 'actorVedioList'),
                                reauestType='GET')
    def actorVedioList(self, urlParams: UrlParams = None):
        logger.info("开始调用" + str(urlParams.url))
        infReturn = HttpUtils.httpGet(urlParams.url, urlParams, params=urlParams.get_param(), headers=urlParams.headMap, verify=False)
        return infReturn


    @CallApiAspect.aroundHandle(CallApiAspect(),
                                servletPath=ReadConfigFile.classNameAndFieldName('actor', 'actorWay'),
                                reauestType='GET')
    def actorWay(self, urlParams: UrlParams = None):
        logger.info("开始调用" + str(urlParams.url))
        infReturn = HttpUtils.httpGet(urlParams.url, urlParams, params=urlParams.get_param(), headers=urlParams.headMap, verify=False)
        return infReturn

    @CallApiAspect.aroundHandle(CallApiAspect(),
                                servletPath=ReadConfigFile.classNameAndFieldName('actor', 'actorFilmV2'),
                                reauestType='GET')
    def actorFilmV2(self, urlParams: UrlParams = None):
        logger.info("开始调用" + str(urlParams.url))
        infReturn = HttpUtils.httpGet(urlParams.url, urlParams, params=urlParams.get_param(), headers=urlParams.headMap, verify=False)
        return infReturn

    @CallApiAspect.aroundHandle(CallApiAspect(),
                                servletPath=ReadConfigFile.classNameAndFieldName('actor', 'actorFilmV3'),
                                reauestType='GET')
    def actorFilmV2(self, urlParams: UrlParams = None):
        logger.info("开始调用" + str(urlParams.url))
        infReturn = HttpUtils.httpGet(urlParams.url, urlParams, params=urlParams.get_param(), headers=urlParams.headMap,
                                      verify=False)
        return infReturn

    @CallApiAspect.aroundHandle(CallApiAspect(),
                                servletPath=ReadConfigFile.classNameAndFieldName('actor', 'relatedActorList'),
                                reauestType='GET')
    def actorFilmV2(self, urlParams: UrlParams = None):
        logger.info("开始调用" + str(urlParams.url))
        infReturn = HttpUtils.httpGet(urlParams.url, urlParams, params=urlParams.get_param(), headers=urlParams.headMap,
                                      verify=False)
        return infReturn

    @CallApiAspect.aroundHandle(CallApiAspect(),
                                servletPath=ReadConfigFile.classNameAndFieldName('actor', 'getActorDesc'),
                                reauestType='GET')
    def actorFilmV2(self, urlParams: UrlParams = None):
        logger.info("开始调用" + str(urlParams.url))
        infReturn = HttpUtils.httpGet(urlParams.url, urlParams, params=urlParams.get_param(), headers=urlParams.headMap,
                                      verify=False)
        return infReturn
