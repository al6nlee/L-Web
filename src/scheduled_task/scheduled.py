import time

from flask_apscheduler import APScheduler


class Config(object):
    JOBS = [
        {
            'id': 'job1',  # 一个标识
            'func': 'src.scheduled_task.scheduled:job1',  # 指定运行的函数
            'args': (1, 2),  # 传入函数的参数
            'trigger': 'cron',  # 指定 定时任务的类型
            # 'seconds': 3600  # 运行的间隔时间
            'minute': '*',
        }
    ]
    SCHEDULER_API_ENABLED = True


# 运行的定时任务的函数
def job1(a, b):
    print(f'This is a timed task demo! results: {a + b}')


scheduler = APScheduler()
