import json
from CallApiLayer.ActorCallApi import ActorCallApi
from aspect.TestCaseAspect import TestCaseAspect
from bean.UrlParams import UrlParams
from utils import JsonUtils


class ActorTestCase:
    # 影人相关直接一个方法融合
    @TestCaseAspect.testCaseListen
    def testActorIdByMovieId(self):
        params = UrlParams()
        p = {'movie_id': '60358', 'page_num': '1', 'page_size': 1}
        params.set_param(p)
        actor_id = ActorCallApi().actorListByMovieId(params)
        JsonUtils.json_data_check(actor_id, 'actorField')
        val = json.loads(actor_id)
        content_ = val['content']
        data_ = content_['data']
        for actorList in data_:
            actor_id = actorList['actor_id']
            p = {'actor_id': actor_id}
            params.set_param(p)
            # 影人星路历程
            ActorCallApi().actorWay(params)
            p = {'actor_id': actor_id, 'page_num': 1, 'page_size': 1}
            params.set_param(p)
            # 影人小视频
            ActorCallApi().actorVedioList(params)
            # 影人资料
            ActorCallApi().actorFilm(params)
            ActorCallApi().relatedActorById(params)






