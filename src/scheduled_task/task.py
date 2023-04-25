import time

from flask_apscheduler import APScheduler

"""
定义定时任务
"""

scheduler = APScheduler()


# interval examples
@scheduler.task('interval', id='do_job_1', seconds=3)
def job1():
    print('每隔3秒执行')


# cron examples
@scheduler.task('cron', id='do_job_2', minute='*')
def job2():
    print('每分钟执行')


@scheduler.task('cron', id='do_job_3', week='*', day_of_week='sun')
def job3():
    print('Job 3 executed')


if __name__ == "__main__":
    scheduler.start()
    while True:
        time.sleep(1)
