from CallApiLayer.UserCallApi import UserCallApi
from aspect.TestCaseAspect import TestCaseAspect
from bean.UrlParams import UrlParams
from config import GlobalConfig
from utils import JsonUtils


class UserTestCase:

    @TestCaseAspect.testCaseListen
    def testAddFeedback(self):
        params = UrlParams()
        p = {"platform": "1", "app_version": "5.1.9", "user_id": "34427118", "phone": "13732491375", "feedback_type": "1",
             "content": "22222", "imags": []}
        params.set_param(p)
        feedback = UserCallApi().addFeedback(params)
        JsonUtils.json_data_check(feedback, 'searchField')

    @TestCaseAspect.testCaseListen
    def testUserPraiseStatus(self):
        params = UrlParams()
        p = {"user_id": GlobalConfig.getGlobalPumkinUserId(), "movie_id": "11652"}
        params.set_param(p)
        status = UserCallApi().userPraiseStatus(params)
        JsonUtils.json_data_check(status, 'searchField')

    @TestCaseAspect.testCaseListen
    def testUserCollectionStatus(self):
        params = UrlParams()
        p = {"user_id": GlobalConfig.getGlobalPumkinUserId(), "movie_id": "11652"}
        params.set_param(p)
        status = UserCallApi().userCollectionStatus(params)
        JsonUtils.json_data_check(status, 'searchField')

    @TestCaseAspect.testCaseListen
    def testUserFanList(self):
        status = UserCallApi().userFanList()
        JsonUtils.json_data_check(status, 'searchField')

    @TestCaseAspect.testCaseListen
    def testUserSecretConfig(self):
        status = UserCallApi().userSecretConfig()
        JsonUtils.json_data_check(status, 'searchField')

    @TestCaseAspect.testCaseListen
    def testFollowAndCancel(self):
        params = UrlParams()
        # 取消关注
        p = {"follow_user_id": GlobalConfig.getGlobalPumkinUserId(), "be_followed_user_id": "6479", "type": "2"}
        params.set_param(p)
        cancel = UserCallApi().followAndCancel(params)
        # 关注
        p = {"follow_user_id": GlobalConfig.getGlobalPumkinUserId(), "be_followed_user_id": "6479", "type": "1"}
        params.set_param(p)
        cancel = UserCallApi().followAndCancel(params)



