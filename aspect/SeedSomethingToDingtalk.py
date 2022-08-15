# -*-coding:utf-8-*-
import requests
import json
import hashlib
import base64
import time
import hmac
import urllib


# https://open.dingtalk.com/document/robots/message-types-and-data-format
# 日志格式说明文档
class send_Something_to_dingTalk():
    def __init__(self):
        self.token = "433fe7ff07dc62c4ce3c69cdb14172d0736715fe856cbd9d152c67993397ec8f"
        self.secret = 'SECcb833eb16c1f42388be72f01c5280cbc8161b7808470ea74ad60d797bba9b34e'  # 这里填写机器人给你的那个签名
        self.headers = {"content-type": "application/json"}
        self.url = ''

    def signGet(self):
        timestamp = str(round(time.time() * 1000))
        secret_enc = self.secret.encode('utf-8')
        string_to_sign = '{}\n{}'.format(timestamp, self.secret)
        string_to_sign_enc = string_to_sign.encode('utf-8')
        hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
        sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
        url = "https://oapi.dingtalk.com/robot/send?access_token=" + str(self.token) + "&timestamp=" + str(timestamp) + "&sign=" + str(sign)
        return url

    def sendActionCard(self, data_dic):
        self.url = self.signGet()
        data = {
            "msgtype": "actionCard",
            "actionCard":
                {
                    "title": "线上android打包情况",
                    "text": "读万卷书，行万里路",
                    "hideAvatar": "0",
                    "btnOrientation": "0",
                    "btns": data_dic,
                }
        }
        res = requests.post(url=self.url, headers=self.headers, data=json.dumps(data))
        print(res.text)


    def seedText(self, text):
        self.url = self.signGet()
        data = {
            "at": {
                "atMobiles": ["13732491375"],
                "isAtAll": "false"
            },
            "text": {
                "content": str(text)
            },
            "msgtype": "text"
        }
        res = requests.post(url=self.url, headers=self.headers, data=json.dumps(data))
        print(res.text)

    def sendMarkdown(self, filename):
        self.url = self.signGet()
        data = {
            "msgtype": "markdown",
            "markdown": {
                "title": "昨日崩溃",
                "test": filename
                },
            "at":
                {
                "atMobiles": ["13732491375"],
                "atUserIds": [],
                "isAtAll": "false"
            }
        }
        res = requests.post(url=self.url, headers=self.headers, data=json.dumps(data))
        print(res.text)

