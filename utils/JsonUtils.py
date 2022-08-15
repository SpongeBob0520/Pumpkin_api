import json
import re

from config import ReadConfigFile, GlobalConfig
from logger.logge import logger

"""
isinstance() 函数来判断一个对象是否是一个已知的类型，类似 type()
isinstance() 与 type() 区别：
    type() 不会认为子类是一种父类类型，不考虑继承关系。
    isinstance() 会认为子类是一种父类类型，考虑继承关系。
"""


# 检查单接口,直接使用json不使用内部类进行检测--json_data接口返回的数据要检测的数据,json_check_field需要检测的类名，提供类名直接获取到配置文件中的字段数据
def json_data_check(json_data, json_check_classname):
    logger.info("需要校验的json：" + str(json_data) + "校验字段列表：" + str(json_check_classname))
    # 非集合类型的json直接进入对象解析
    if type(json_data) != type([]):
        k = json_data
        # 非字典类型需要进行转化
        if not isinstance(json_data, dict):
            k = json.loads(json_data)
        # 取出原json中所有的key
        keys = k.keys()
        for key in keys:
            #  获取key对应的value
            # 取出的值 判断是否为集合如果是集合则需要进入,进行下一步obj解析
            if type(k[key]) == type([]):
                # 取出集合对象
                key_obj = k[key]
                for obj_data in key_obj:
                    # 将单个对象重新赋值进入
                    json_data_check(json.dumps(obj_data, ensure_ascii=False), json_check_classname)
            else:
                # 获取配置文件中需要检查的字段
                # 在校验json找到 被检查json中的key说明需要校验
                response_class_list = ReadConfigFile.classNameAndFieldName(json_check_classname)
                if str(response_class_list).find(str(key)) >= 0:
                    # 需要被检查的值
                    get_key_target = k[key]
                    # 如果是字典类型直接复制即可无需转化
                    loads = response_class_list
                    # 获取正则表达式 --非字典需要进行转化
                    if not isinstance(response_class_list, dict):
                        loads = json.loads(response_class_list)
                    value_regular = loads[str(key)]
                    match = re.findall(str(value_regular), str(get_key_target))
                    if match is None:
                        # 此处将总报告设置为失败
                        reportRoot = GlobalConfig.getReportClassInfo()
                        reportRoot.set_result(False)
                        # 此处要抛出异常，说明该条用例执行失败
                        raise Exception(
                            '字段校验失败,请检查,字段名:' + key + "接口返回值: " + get_key_target + " 需要符合的规则" + str(value_regular))

    else:
        # 是集合对象则需要将集合对象一一取出来进行内嵌反调回去进行对象解析
        k = json.loads(json_data)
        for obj_data in k:
            json_data_check(json.dumps(obj_data, ensure_ascii=False), json_check_classname)


class JsonUtils:

    def __init__(self):
        """初始化全局变量，其实可以直接设置成属性，写都写了就不想改了"""
        GlobalConfig.setBecursionFlag(True)

    """
    特别注意：因为递归的特殊性，如果需要强制退出就需要全局变量进行控制，所以使用该方法时需要重新创建新的class用来初始化全局变量
    """
    # 该方法使用方式 -传入json,指定key检索json中你需要的key并返回，当json中出现多个相同key时只会返回第一个
    def getJsonAppointFiledVal(self, json_data, fieldNameRequired: str):
        if json_data is not None and json_data != '':
            if not GlobalConfig.getBecursionFlag():
                return GlobalConfig.getResultJson()
            logger.info("需要解析的json: " + str(json_data))
            # 非集合类型的json直接进入对象解析
            if type(json_data) != type([]):
                k = json_data
                # 非字典类型需要进行转化
                if not isinstance(json_data, dict):
                    k = json.loads(json_data)
                # 取出原json中所有的key
                keys = k.keys()
                for key in keys:
                    #  如果传入的字段名称对应的值是列表直接将列表返回
                    if str(key) == fieldNameRequired:
                        # 找到该字段，直接将值返回出去
                        resultTarget = k[key]
                        GlobalConfig.setBecursionFlag(False)
                        GlobalConfig.setResultJson(str(resultTarget))
                        return GlobalConfig.getResultJson()
                    # 取出的值 判断是否为集合如果是集合则需要进入,进行下一步obj解析
                    if type(k[key]) == type([]):
                        # 取出集合对象
                        key_obj = k[key]
                        for obj_data in key_obj:
                            # 将单个对象重新赋值进入
                            self.getJsonAppointFiledVal(json.dumps(obj_data, ensure_ascii=False), fieldNameRequired)
                    elif str(key) == fieldNameRequired:
                        # 找到该字段，直接将值返回出去
                        resultTarget = k[key]
                        GlobalConfig.setBecursionFlag(False)
                        GlobalConfig.setResultJson(str(resultTarget))
                        return GlobalConfig.getResultJson()
            else:
                # 是集合对象则需要将集合对象一一取出来进行内嵌反调回去进行对象解析
                k = json_data
                if not isinstance(json_data, dict):
                    k = json.loads(json_data)
                for obj_data in k:
                    self.getJsonAppointFiledVal(json.dumps(obj_data, ensure_ascii=False), fieldNameRequired)
            if not GlobalConfig.getBecursionFlag():
                return GlobalConfig.getResultJson()


class tts:
    if __name__ == '__main__':
        s = {"movie_id": 25804, "movie_name": "三国演义", "movie_image_url": "https://m-image.vcinema.cn/OnAqUX44T8t1LoedPfp5xwsN.png?x-oss-process=image/interlace,1/resize,m_fill,w_<width>,h_<height>/quality,q_100/sharpen,100/format,jpg", "movie_director": "王扶林,张绍林,蔡晓晴,孙光明,张中一,沈好放", "movie_actor": "唐国强,孙彦军,鲍国安,李靖飞,陆树铭,洪宇宙,吴晓东", "movie_country": "中国", "movie_year": "1994", "movie_type": 2, "is_user_favorite": 0, "movie_index": "G1-1", "icon_color": "", "movie_status_int": 0, "movie_vertical_pic": "https://m-image-v2.vcinema.cn/OnAqUX44T8t1LoedPfp5xwsN.png?x-oss-process=image/auto-orient,1/resize,m_fixed,w_<width>,h_<height>/quality,Q_100/format,webp", "need_seed_number_str": "", "need_seed_desc_str": "", "seed_movie_status_int": 0, "exchange_status_int": 0, "effect_time_desc": "", "movie_score": "9.3", "movie_watch_count": 0, "due_user_status": "false", "deluxe_ready": "false", "drm_status": "false", "playback_speed_status": "false", "trailler_id": "", "prevue_status": "false", "movie_category": "精选"}

        li = ['ALL', 'MOVIE', 'SERIES']
        index = li[1]
        print(index)
