from CallApiLayer.QrCodeCallApi import QrCodeCallApi
from aspect.TestCaseAspect import TestCaseAspect


class QrCodeTestCase:

    # 二维码相关
    @TestCaseAspect.testCaseListen
    def testQrCode(self):
        QrCodeCallApi().praiseComentList()
        QrCodeCallApi().contactUsQrCodeV2()
        QrCodeCallApi().associationQrCode()
        QrCodeCallApi().writtenQrCode()
        QrCodeCallApi().writtenQrCodeV2()
        QrCodeCallApi().bulletScreenQrCode()
        QrCodeCallApi().feedBackQrCode()
        # QrCodeCallApi().jumpQrCode()
        # QrCodeCallApi().lawQrCode()
        # QrCodeCallApi().loginQrCode()
        # QrCodeCallApi().redirectLiveQrCode()
        # QrCodeCallApi().tpaidQrCode()