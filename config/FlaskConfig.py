from flask import Flask, render_template
from flask_apscheduler import APScheduler
from aspect.StartInitData import StartInitData
from config.SchedulerConfig import SchedulerConfig

flask = Flask(__name__)
# flask.config.from_object(Config)
# 引入定时任务配置
flask.config.from_object(SchedulerConfig())
# 声明定时任务组件
scheduler = APScheduler()
# 初始化定时任务
scheduler.init_app(flask)
# 启动定时任务
scheduler.start()
StartInitData().loadConfig()
flask.config["JSON_AS_ASCII"] = False
