from flask import Flask

from src.scheduled_task.scheduled import Config, scheduler

app = Flask(__name__)


@app.route('/index', methods=['GET'])
@app.route('/', methods=['GET'])
def index():  # put application's code here
    """
    首页
    :return:
    """
    return 'Hello World!'


@app.after_request
def after_request(response):
    """
    配合前端设置允许跨域等请求后处理操作
    """
    return response


# 定时任务功能code began
app.config.from_object(Config)
scheduler.init_app(app)
scheduler.start()
# 定时任务功能code end


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
