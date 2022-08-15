from aspect.CallApiAspect import CallApiAspect
from bean.CheckException import CheckException
from bean.UrlParams import UrlParams
from config import ReadConfigFile
from httpSendRequest import HttpUtils
from logger.logge import logger


class HomeCallApi:

    # 获取首页的默认类型:电影/剧集/首页
    @CallApiAspect.aroundHandle(CallApiAspect(), servletPath=ReadConfigFile.classNameAndFieldName('home', 'catgConf'), reauestType='GET')
    def homeAllType(self,urlParams: UrlParams = None):
        logger.info("开始调用"+str(urlParams.url))
        infReturn = HttpUtils.httpGet(urlParams.url, urlParams, headers=urlParams.headMap)
        return infReturn

    # 获取电影类别下的所有组件
    @CallApiAspect.aroundHandle(CallApiAspect(), servletPath=ReadConfigFile.classNameAndFieldName('home', 'movieHomeInfo'), reauestType='GET')
    def getHomeMoiveAssemblyAll(self,urlParams: UrlParams = None):
        logger.info("开始调用" + str(urlParams.url))
        infReturn = HttpUtils.httpGet(urlParams.url, urlParams, headers=urlParams.headMap)
        return infReturn

    # 获取电视剧类别下的所有组件
    @CallApiAspect.aroundHandle(CallApiAspect(), servletPath=ReadConfigFile.classNameAndFieldName('home', 'seriousHomInfo'), reauestType='GET')
    def getHomeSeriousAssemblyAll(self,urlParams: UrlParams = None):
        logger.info("开始调用" + str(urlParams.url))
        infReturn = HttpUtils.httpGet(urlParams.url, urlParams, headers=urlParams.headMap)
        return infReturn

    # 获取首页类别下的所有组件
    @CallApiAspect.aroundHandle(CallApiAspect(), servletPath=ReadConfigFile.classNameAndFieldName('home', 'seriousHomInfo'), reauestType='GET')
    def getHomeNormalHomeAssemblyAll(self,urlParams: UrlParams = None):
        logger.info("开始调用" + str(urlParams.url))
        infReturn = HttpUtils.httpGet(urlParams.url, urlParams, headers=urlParams.headMap)
        return infReturn

    # 多次请求接口返回无需刷新
    @CallApiAspect.aroundHandle(CallApiAspect(), servletPath=ReadConfigFile.classNameAndFieldName('home', 'seriousHomInfo'), reauestType='GET')
    def doubleRequestCheck(self,urlParams: UrlParams = None):
        logger.info("开始调用" + str(urlParams.url))
        # 第一次请求会给标准数据
        HttpUtils.httpGet(urlParams.url, urlParams, headers=urlParams.headMap)
        # 紧接着继续请求,会返回提示
        infReturn = HttpUtils.httpGet(urlParams.url, urlParams, headers=urlParams.headMap)
        logger.info("接口返回结果：" + str(infReturn))
        if infReturn.find('无需刷新') < 0:
            raise CheckException('返回结果有误,预期为无需刷新，请检查,接口地址：'+str(urlParams.url)+' 接口返回值：'+str(infReturn))
        return infReturn

    # 获取指定类别下的电影/电视剧类型-如动作,科幻等，参数写入urlParams.param中
    @CallApiAspect.aroundHandle(CallApiAspect(), servletPath=ReadConfigFile.classNameAndFieldName('home', 'temCatList'), reauestType='GET')
    def getHomeMovieType(self,urlParams: UrlParams = None):
        logger.info("开始调用" + str(urlParams.url))
        infReturn = HttpUtils.httpGet(urlParams.url, urlParams, params=urlParams.get_param(), headers=urlParams.headMap)
        return infReturn

    # 获取类别下的组件，例如：科幻下的组件id和名称就是通过这个接口获取的
    @CallApiAspect.aroundHandle(CallApiAspect(), servletPath=ReadConfigFile.classNameAndFieldName('home', 'mainHomeInfo'), reauestType='GET')
    def getMoiveTypeAssembly(self,urlParams: UrlParams = None):
        logger.info("开始调用" + str(urlParams.url))
        infReturn = HttpUtils.httpGet(urlParams.url, urlParams, params=urlParams.get_param(), headers=urlParams.headMap)
        return infReturn

    # 获取指定组件下的电影资源
    @CallApiAspect.aroundHandle(CallApiAspect(), servletPath=ReadConfigFile.classNameAndFieldName('home', 'catgDetailInfo'), reauestType='GET')
    def getMovieResources(self,urlParams: UrlParams = None):
        logger.info("开始调用" + str(urlParams.url))
        infReturn = HttpUtils.httpGet(urlParams.url, urlParams, params=urlParams.get_param(), headers=urlParams.headMap)
        return infReturn

    @CallApiAspect.aroundHandle(CallApiAspect(), servletPath=ReadConfigFile.classNameAndFieldName('home', 'trailerPlayMovieId'), reauestType='POST')
    def getTrailerPlayMovieId(self,urlParams: UrlParams = None):
        logger.info("开始调用" + str(urlParams.url))
        infReturn = HttpUtils.httpPost(urlParams.url, urlParams, data=urlParams.get_param(), headers=urlParams.headMap)
        return infReturn

    # tv首页默认小视频的值
    @CallApiAspect.aroundHandle(CallApiAspect(), servletPath=ReadConfigFile.classNameAndFieldName('home', 'homeBanner'), reauestType='GET')
    def homeV50(self,urlParams: UrlParams = None):
        infReturn = HttpUtils.httpGet(urlParams.url, urlParams, headers=urlParams.headMap)
        return infReturn


