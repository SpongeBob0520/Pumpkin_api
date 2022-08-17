# 任务配置类
from config.GlobalConfig import setGlobalPumPkinToken

# 定时任务配置
class SchedulerConfig(object):
    # 配置执行job
    JOBS = [
        {
            'id': 'put_into_queue',
            'func': setGlobalPumPkinToken,
            'args': None,
            'trigger': 'interval',
            'seconds': 60*60*4  # 本任务为每4小时执行一次
        },

    ]
    # # 存储位置
    # SCHEDULER_JOBSTORES = {
    #     'default': SQLAlchemyJobStore(url='sqlite:///jobs.sqlite')
    # }
    # 线程池配置
    SCHEDULER_EXECUTORS = {
        'default': {'type': 'threadpool', 'max_workers': 20}
    }
    # 配置时区
    SCHEDULER_TIMEZONE = 'Asia/Shanghai'
    SCHEDULER_JOB_DEFAULTS = {
        'coalesce': False,
        'max_instances': 3
    }
    # 调度器开关
    SCHEDULER_API_ENABLED = True
