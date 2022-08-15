import re

from CallApiLayer.MovieCallApi import MovieCallApi
from aspect.TestCaseAspect import TestCaseAspect
from bean.UrlParams import UrlParams
from config import ReadConfigFile, GlobalConfig
from utils import JsonUtils


class MovieTestCase:

    # drm
    @TestCaseAspect.testCaseListen
    def testDrmPlayMovieUrl(self):
        p ={'movie_id':'11652','user_id':GlobalConfig.getGlobalPumkinUserId()}
        params = UrlParams()
        params.set_param(p)
        drmUrl = MovieCallApi().drmPlayMovieUrl(params)
        JsonUtils.json_data_check(drmUrl, 'movieField')

    # 类似影视
    @TestCaseAspect.testCaseListen
    def testMovieSimilerMovie(self):
        p = {'movie_id': '60358', 'user_id': GlobalConfig.getGlobalPumkinUserId()}
        params = UrlParams()
        params.set_param(p)
        movie = MovieCallApi().movieSimilerMovie(params)
        JsonUtils.json_data_check(movie,'movieField')

    # 获取更多预告片
    @TestCaseAspect.testCaseListen
    def testMoreSearchReservation(self):
        p = {'movie_id': '13053', 'page_num': 1,'page_size':1}
        params = UrlParams()
        params.set_param(p)
        reservation = MovieCallApi().moreSearchReservation(params)
        JsonUtils.json_data_check(reservation,'movieField')

    # 预约
    @TestCaseAspect.testCaseListen
    def testSearchReservation(self):
        # 预约
        p = {'movie_id': '10445', 'status': 1, 'user_id': GlobalConfig.getGlobalPumkinUserId()}
        params = UrlParams()
        params.set_param(p)
        reservation = MovieCallApi().addOrDelReservation()
        JsonUtils.json_data_check(reservation, 'movieField')
        # 查询预约情况
        pf = {'movie_id': '10445','page_num':1,'page_size':5}
        params.set_param(pf)
        search_reservation = MovieCallApi().moreSearchReservation(params)
        JsonUtils.json_data_check(search_reservation,'movieField')
        # 取消预约
        p = {'movie_id': '10445', 'status': 0, 'user_id': GlobalConfig.getGlobalPumkinUserId()}
        params = UrlParams()
        params.set_param(p)
        reservation = MovieCallApi().addOrDelReservation()
        JsonUtils.json_data_check(reservation, 'movieField')

        # 查询预约情况
        pf = {'movie_id': '10445', 'page_num': 1, 'page_size': 5}
        params.set_param(pf)
        search_reservation = MovieCallApi().moreSearchReservation(params)
        JsonUtils.json_data_check(search_reservation, 'movieField')

    # 用户观影历史
    @TestCaseAspect.testCaseListen
    def testUserMovieRecord(self):
        params = UrlParams()
        pf = {'user_id': GlobalConfig.getGlobalPumkinUserId(), 'page_num': 1, 'page_size': 10}
        params.set_param(pf)
        record = MovieCallApi().userMovieRecord(params)
        JsonUtils.json_data_check(record,'movieField')

    # 喜欢影视
    @TestCaseAspect.testCaseListen
    def testLikeMovie(self):
        params = UrlParams()
        pf = {'user_id': GlobalConfig.getGlobalPumkinUserId(), 'page_num': 1, 'page_size': 10}
        params.set_param(pf)
        movie = MovieCallApi().likeMovie(params)
        JsonUtils.json_data_check(movie, 'movieField')

    # 根据电影id获取电影信息
    @TestCaseAspect.testCaseListen
    def testMovieInfoById(self):
        params = UrlParams()
        name = ReadConfigFile.classNameAndFieldName('movie', 'movieInfoById')
        newName = name+'/'+GlobalConfig.getGlobalPumkinUserId()+'/'+'60358/0'
        name = newName
        by_id = MovieCallApi().getMovieInfoById()
        JsonUtils.json_data_check(by_id,'movieField')

    # 点击导视获取电影详情
    @TestCaseAspect.testCaseListen
    def testTrailerDesc(self):
        params = UrlParams()
        p = {'movie_id':'60358'}
        params.set_param(p)
        desc = MovieCallApi().trailerDesc(params)
        JsonUtils.json_data_check(desc, 'movieField')
