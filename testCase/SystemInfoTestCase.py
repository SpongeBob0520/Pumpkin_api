from CallApiLayer.SystemInfoCallApi import SystemInfoCallApi
from aspect.TestCaseAspect import TestCaseAspect
from bean.UrlParams import UrlParams
from config import GlobalConfig


class SystemInfoTestCase:

    @TestCaseAspect.testCaseListen
    def testSystemInfo(self):
        params = UrlParams()
        p = {'page_num':1,'page_size':1,'user_id': GlobalConfig.getGlobalPumkinUserId()}
        params.set_param(p)
        coment_list = SystemInfoCallApi().praiseComentList(params)
        p = {'platform':'APH', 'user_id': GlobalConfig.getGlobalPumkinUserId()}
        params.set_param(p)
        navgation = SystemInfoCallApi().remindNavgation(params)
        p = {'platform': '1', 'user_id': GlobalConfig.getGlobalPumkinUserId()}
        params.set_param(p)
        status = SystemInfoCallApi().updateRemindStatus(params)
        p = {'contact_user_id': '2679', 'user_id': GlobalConfig.getGlobalPumkinUserId()}
        params.set_param(p)
        remind_status = SystemInfoCallApi().remindStatus(params)

    # tv屏保
    @TestCaseAspect.testCaseListen
    def testScreenRotation(self):
        params = UrlParams()
        p = {'user_id': GlobalConfig.getGlobalPumkinUserId()}
        params.set_param(p)
        SystemInfoCallApi().screenRotation(params)


