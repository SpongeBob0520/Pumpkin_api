配置文件编写：
1.在resource文件夹下 application.ini文件下，按照模块命名 section 然后添加接口
2.添加接口的时候注意，不允许自己命名，只能吧接口的下划线原则转换成驼峰原则来命名例如：影人的section名字就叫 actor 下面的接口命名规范如下
actorFilmV3: /actor/get_actor_films_v3!
底层接口访问方法：
1.需要在CallApiLayer文件夹下新建该模块下的py文件 按照 模块+CallApi固定格式命名 如 影人就是 ActorCallApi.py，这个也是固定格式的，不要自己取名字，该文件下需要新建类，类名和文件名保持一致
2.类方法编写格式如下：
    2.1 方法命名：按照你接口名字命名，如上面actorFilmV3接口，这个接口访问方法名字就叫actorFilmV3
    2.2 方法：按照固定格式修修改改就行
    @CallApiAspect.aroundHandle(CallApiAspect(), servletPath=ReadConfigFile.classNameAndFieldName(接口所在section的name 接口名字), reauestType=请求方式)
    def 这边就是接口名字(self, urlParams: UrlParams = None):
        logger.info("开始调用" + str(urlParams.url))
        infReturn = HttpUtils.httpGet(urlParams.url, urlParams, params=urlParams.get_param(), headers=urlParams.headMap, verify=False)
        return infReturn
    2.3 这就是写好一个接口的底层访问方法类了，接下来需要分装成具体的测试用例
测试用例编写：
1.在testCase文件夹下新增你编写模块的py文件，按照 模块+TestCase 固定格式命名 如影人就是 ActorTestCase.py。固定格式，不允许自己发挥取名字，该文件下新建类，类名与文件名保持一致
2.类方法编写格式如下：
    2.1 目前只要求一条测试用例，即串联整个模块下全部接口，形成闭环，除用户信息和movie_id以外信息，其他信息不允许在代码写死，需要从接口获取，来传值给下一个接口
    2.2 例如影人接口的访问我是写死一个movie_id是 60358 第一个分页下全部影人都会访问一遍代码如下：
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
    2.3 以上情况有出入或者某些场景下必须写死，找蒋南强说明理由和情况，除非情况特殊，否则在原则上不允许存在代码写死数据情况
用例执行
用例的执行可以在用例文件夹下面建main方法快速调试执行，但是代码在上传之前必须做以下操作，自测通过才能push到git
1.找到controller文件夹下，找到RestController.py文件 修改postMethod方法，按照你的情况修改以下模版
    只需要全部注释postMethod方法下全部内容，然后按照你的情况修改以下模版
    envPrifx = request.args.get('envPrifx')
    phone = request.args.get('phone')
    # 更新环境数据
    updataEnvInfoConfig(envPrifx, phone)
    ###    
    你的测试用例
    ###
    globleReport = GlobalConfig.getReportClassInfo()
    return ResponseUtils.reportToStrModelAndView(globleReport)
2.执行 右键启动RestController.py项目后，通过浏览器访问http://127.0.0.1:5000/notice 
接口响应给你一个测试报告（全都是json格式的内容），说明你这边执行就是OK的，确认没问题后，push代码到git，找蒋南强审核代码
注意事项：这个版本我是注释了钉钉机器人的，不会给你们开启，否则消息太烦人了，出来以上涉及的文件夹，其他文件夹下文件不可用动，有需要动，找蒋南强
不要动别的文件！！！！！！！！！
不要动别的文件！！！！！！！！！
不要动别的文件！！！！！！！！！
不要动别的文件！！！！！！！！！
不要动别的文件！！！！！！！！！
服务器上面的部署和执行统一由蒋南强来完成，原则上不需要你们来动