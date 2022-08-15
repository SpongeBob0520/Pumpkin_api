from CallApiLayer.SearchCallApi import SearchCallApi
from aspect.TestCaseAspect import TestCaseAspect
from bean.UrlParams import UrlParams
from utils.JsonUtils import JsonUtils


class SearchTestCase:

    # 热门搜索
    @TestCaseAspect.testCaseListen
    def testSearchHot(self):
        search_hot = SearchCallApi().searchHot()
        JsonUtils().getJsonAppointFiledVal(search_hot, 'hotField')

    # 关键词搜索
    @TestCaseAspect.testCaseListen
    def testSearchKeyWords(self):
        params = UrlParams()
        params.set_param({'keyword': '龙'})
        word = SearchCallApi().searchKeyWord(params)
        JsonUtils().getJsonAppointFiledVal(word, 'hotField')

    # Tv搜索过滤
    @TestCaseAspect.testCaseListen
    def testTvSearchKeyWords(self):
        params = UrlParams()
        params.set_param({'search_key': '龙', 'page_size': 30, 'page_num': 2})
        word = SearchCallApi().searchTvKeyWord(params)
        JsonUtils().getJsonAppointFiledVal(word, 'hotField')

    # 点我求片
    @TestCaseAspect.testCaseListen
    def testAskClickSearchMovie(self):
        params = UrlParams()
        params.set_param({'keyword': 'oooo'})
        movie = SearchCallApi().askClickSearchMovie(params)
        JsonUtils().getJsonAppointFiledVal(movie, 'hotField')

    # 获取搜索图标
    @TestCaseAspect.testCaseListen
    def testConfSearchIcons(self):
        icons = SearchCallApi().confSearchIcons()
        JsonUtils().getJsonAppointFiledVal(icons, 'hotField')
