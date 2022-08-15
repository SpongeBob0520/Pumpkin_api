import json

from CallApiLayer.HomeCallApi import HomeCallApi
from aspect.TestCaseAspect import TestCaseAspect
from bean.UrlParams import UrlParams
from utils import JsonUtils


class HomeTestCase:

    # 获取首页的所有类型  全部-电影-剧集
    @TestCaseAspect.testCaseListen
    def testHom(self):
        homeType = HomeCallApi().homeAllType()
        JsonUtils.json_data_check(homeType, 'homeField')

    # 获取指定类型下的组件,
    @TestCaseAspect.testCaseListen
    def testHomeNormalHomeAssemblyAll(self):
        # 全部，电影，剧集
        # li = ['ALL','MOVIE','SERIES']
        # params = UrlParams()
        # for key in li:
        #     params.set_param(key)
        assembly_all = HomeCallApi().getHomeNormalHomeAssemblyAll()
        JsonUtils.json_data_check(assembly_all, 'homeField')

    # 获取获取指定类别下的电影/电视剧类型-如动作,科幻等
    @TestCaseAspect.testCaseListen
    def testHomeAssemblyAllResources(self):
        # 全部，电影，剧集
        li = ['ALL', 'MOVIE', 'SERIES']
        params = UrlParams()
        for key in li:
            params.set_param({"template_mode": key})
            movie_type = HomeCallApi().getHomeMovieType(params)
            JsonUtils.json_data_check(movie_type, 'homeField')

    @TestCaseAspect.testCaseListen
    def testMovieTypeAssemby(self):
        # 全部，电影，剧集
        li = ['ALL', 'MOVIE', 'SERIES']
        params = UrlParams()
        for key in li:
            params.set_param({"template_mode": key})
            movie_type = HomeCallApi().getHomeMovieType(params)
            JsonUtils.json_data_check(str(movie_type), 'homeField')
            loads = json.loads(movie_type)
            content_ = loads['content']
            id_ = content_[1]['category_id']
            params.set_param({"classification_id": str(id_)})
            # 获取类别下的组件
            assembly = HomeCallApi().getMoiveTypeAssembly(params)
            # 检测字段
            JsonUtils.json_data_check(assembly, 'homeField')
            json_loads = json.loads(assembly)
            list_ = json_loads['content']
            info_list_ = list_['home_template_info_list']
            # 获取电影下的资源
            pp = {'tem_id': info_list_[1]['tem_id'], 'tem_prefix': info_list_[1]['tem_id']}
            params.set_param(pp)
            HomeCallApi().getMovieResources(params)

    @TestCaseAspect.testCaseListen
    def testTrailerPlayMovieId(self):
        params = UrlParams()
        li = {"movie_ids": ['62043'], "media_type": "VERTICAL"}
        params.set_param(li)
        HomeCallApi().getTrailerPlayMovieId(params)

    # 检测多次请求的情况下返回错误码的情况
    @TestCaseAspect.testCaseListen
    def testDoubleRequestCheck(self):
        HomeCallApi().doubleRequestCheck()

    # tv首页默认的图片视频列表
    @TestCaseAspect.testCaseListen
    def testHomeInf(self):
        HomeCallApi().homeV50()

    @TestCaseAspect.testCaseListen
    def test(self):
        pass