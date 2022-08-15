import json

from CallApiLayer.HallCallApi import HallCallApi
from aspect.TestCaseAspect import TestCaseAspect
from bean.UrlParams import UrlParams
from config import ReadConfigFile, GlobalConfig
from logger.logge import logger


class HallTestCase:

    def __init__(self):
        self.channel_id = None

    # 创建放映厅
    @TestCaseAspect.testCaseListen
    def testCreatHall(self):
        # 创建放映厅
        hallName = ReadConfigFile.classNameAndFieldName('hall', 'create_channel')
        name = ReadConfigFile.classNameAndFieldName('domainname', 'envPrifx') + '/v5.0' + hallName + '?movie_id=60358&user_id=' + GlobalConfig.getGlobalPumkinUserId()
        params = UrlParams()
        params.set_url(name)
        hall = HallCallApi().ceatHall(params)

        loads = json.loads(hall)
        content_ = loads['content']
        channel_id = content_['channel_id']
        self.channel_id = channel_id

    # 查看放映厅在线人数
    @TestCaseAspect.testCaseListen
    def testPumkinOnlineHall(self):
        onlineUser = HallCallApi().pumkinOnlineHall()

    # 发送弹幕
    @TestCaseAspect.testCaseListen
    def testSendScreenemoji(self):
        urlParams = UrlParams()
        p = {'channel_id':self.channel_id,'movie_id':'60358','play_length':11111,'user_id': GlobalConfig.getGlobalPumkinUserId()}
        urlParams.set_param(p)
        screenemoji = HallCallApi().sendScreenemoji(urlParams)

    # 进入放映厅
    @TestCaseAspect.testCaseListen
    def testAddHall(self):
        urlParams = UrlParams()
        p = {'channel_id':self.channel_id}
        urlParams.set_param(p)
        addHall = HallCallApi().addHall(urlParams)

    # 放映厅历史弹幕
    @TestCaseAspect.testCaseListen
    def testBulletList(self):
        urlParams = UrlParams()
        name = ReadConfigFile.classNameAndFieldName('domainname', 'envPrifx') + '/v5.0' + ReadConfigFile.classNameAndFieldName('hall', 'bulletList') + "/" + self.channel_id
        urlParams.set_param(name)
        bullet_list = HallCallApi().bulletList(urlParams)

    

    # 解散放映厅
    @TestCaseAspect.testCaseListen
    def testDisMissHall(self):
        params = UrlParams()
        disHall = ReadConfigFile.classNameAndFieldName('hall', 'dismissHall')
        disHall = ReadConfigFile.classNameAndFieldName('domainname', 'envPrifx') + '/v5.0' + disHall + "?user_id=" + GlobalConfig.getGlobalPumkinUserId() + "&channel_id=" + self.channel_id
        params.set_url(disHall)
        dismiss_hall = HallCallApi().dismissHall(params)
        logger.info(dismiss_hall)
