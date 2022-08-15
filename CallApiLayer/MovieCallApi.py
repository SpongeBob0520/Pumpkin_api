from aspect.CallApiAspect import CallApiAspect
from bean.UrlParams import UrlParams
from config import ReadConfigFile
from httpSendRequest import HttpUtils
from logger.logge import logger


class MovieCallApi:

    # 获取获取影片的drm地址
    @CallApiAspect.aroundHandle(CallApiAspect(), servletPath=ReadConfigFile.classNameAndFieldName('movie', 'drmPlayMovieUrl'),
                                reauestType='GET')
    def drmPlayMovieUrl(self, urlParams: UrlParams = None):
        logger.info("开始调用" + str(urlParams.url))
        infReturn = HttpUtils.httpGet(urlParams.url, urlParams, headers=urlParams.headMap,verify=False)
        return infReturn

    # 类似影视
    @CallApiAspect.aroundHandle(CallApiAspect(),
                                servletPath=ReadConfigFile.classNameAndFieldName('movie', 'movieSimilerMovie'),
                                reauestType='GET')
    def movieSimilerMovie(self, urlParams: UrlParams = None):
        logger.info("开始调用" + str(urlParams.url))
        infReturn = HttpUtils.httpGet(urlParams.url, urlParams,params=urlParams.get_param(), headers=urlParams.headMap,verify=False)
        return infReturn

    # 更多预告片
    @CallApiAspect.aroundHandle(CallApiAspect(),
                                servletPath=ReadConfigFile.classNameAndFieldName('movie', 'movieMoreTrailer'),
                                reauestType='GET')
    def moreSearchReservation(self, urlParams: UrlParams = None):
        logger.info("开始调用" + str(urlParams.url))
        infReturn = HttpUtils.httpGet(urlParams.url, urlParams,params=urlParams.get_param(), headers=urlParams.headMap,verify=False)
        return infReturn

    # 预约预告片/取消预告片
    @CallApiAspect.aroundHandle(CallApiAspect(),
                                servletPath=ReadConfigFile.classNameAndFieldName('movie', 'addOrDelReservation'),
                                reauestType='GET')
    def addOrDelReservation(self, urlParams: UrlParams = None):
        logger.info("开始调用" + str(urlParams.url))
        infReturn = HttpUtils.httpGet(urlParams.url, urlParams,params=urlParams.get_param(), headers=urlParams.headMap,verify=False)
        return infReturn

    # 用户观影历史
    @CallApiAspect.aroundHandle(CallApiAspect(),
                                servletPath=ReadConfigFile.classNameAndFieldName('movie', 'userMovieRecord'),
                                reauestType='GET')
    def userMovieRecord(self, urlParams: UrlParams = None):
        logger.info("开始调用" + str(urlParams.url))
        infReturn = HttpUtils.httpGet(urlParams.url, urlParams,params=urlParams.get_param(), headers=urlParams.headMap,verify=False)
        return infReturn

    # 用户收藏
    @CallApiAspect.aroundHandle(CallApiAspect(),
                                servletPath=ReadConfigFile.classNameAndFieldName('movie', 'userMovieFavortie'),
                                reauestType='GET')
    def userMovieFavortie(self, urlParams: UrlParams = None):
        logger.info("开始调用" + str(urlParams.url))
        infReturn = HttpUtils.httpGet(urlParams.url, urlParams,params=urlParams.get_param(), headers=urlParams.headMap,verify=False)
        return infReturn

    # 用户喜欢影视
    @CallApiAspect.aroundHandle(CallApiAspect(),
                                servletPath=ReadConfigFile.classNameAndFieldName('movie', 'movieInfoById'),
                                reauestType='GET')
    def likeMovie(self, urlParams: UrlParams = None):
        logger.info("开始调用" + str(urlParams.url))
        infReturn = HttpUtils.httpGet(urlParams.url, urlParams, params=urlParams.get_param(),headers=urlParams.headMap,verify=False)
        return infReturn

    # 根据电影id获取电影信息
    @CallApiAspect.aroundHandle(CallApiAspect(),
                                servletPath=ReadConfigFile.classNameAndFieldName('movie', 'movieInfoById'),
                                reauestType='GET')
    def getMovieInfoById(self, urlParams: UrlParams = None):
        logger.info("开始调用" + str(urlParams.url))
        infReturn = HttpUtils.httpGet(urlParams.url, urlParams, headers=urlParams.headMap,verify=False)
        return infReturn

    @CallApiAspect.aroundHandle(CallApiAspect(),
                                servletPath=ReadConfigFile.classNameAndFieldName('movie', 'movietrailerList'),
                                reauestType='GET')
    def movietrailerList(self, urlParams: UrlParams = None):
        logger.info("开始调用" + str(urlParams.url))
        infReturn = HttpUtils.httpGet(urlParams.url, urlParams,params=urlParams.get_param(), headers=urlParams.headMap,verify=False)
        return infReturn

    @CallApiAspect.aroundHandle(CallApiAspect(),
                                servletPath=ReadConfigFile.classNameAndFieldName('trailer', 'trailerDesc'),
                                reauestType='GET')
    def trailerDesc(self, urlParams: UrlParams = None):
        logger.info("开始调用" + str(urlParams.url))
        infReturn = HttpUtils.httpGet(urlParams.url, urlParams, params=urlParams.get_param(), headers=urlParams.headMap,
                                      verify=False)
        return infReturn