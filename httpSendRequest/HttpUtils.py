import json

import requests

from aspect.HttpAspect import HttpAspect
from config import GlobalConfig

from logger.logge import logger


@HttpAspect.httpListen
def httpGet(url, urlparams, **kwargs) -> str:
    logger.info("GET请求传入的参数：" + str(urlparams.param))
    logger.info("GET的请求链接：" + str(url))
    response = requests.get(url, **kwargs)
    # 将返回结果记录进入全局变量
    GlobalConfig.setInterResponse(response)
    requests.session().close()
    logger.info("GET请求的请求头：" + str(urlparams.headMap))
    logger.info("GET请求响应数据：" + str(response.content.decode('utf8')))
    return str(response.content.decode('utf8'))


@HttpAspect.httpListen
def httpPost(url, urlparams, **kwargs):
    logger.info("POST请求传入的参数：" + str(urlparams.param))
    logger.info("POST的请求链接：" + url)
    response = requests.post(url, **kwargs)
    # 将返回结果记录进入全局变量
    GlobalConfig.setInterResponse(response)
    requests.session().close()
    logger.info("POST请求的请求头：" + str(urlparams.headMap))
    logger.info("POST请求响应数据：" + str(response.content.decode('utf8')))
    return str(response.content.decode('utf8'))
