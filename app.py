import datetime
import os

from redis import Redis
from flask import Flask, request, Response, jsonify, redirect, session, render_template
from flask_session import Session
from src.scheduled_task.scheduled import Config, scheduler
from src.utils.conf_section import get_conf_section
from src.utils.validate_request import validate_request

app = Flask(__name__)


@app.route('/index', methods=['GET'])
@app.route('/', methods=['GET'])
def index():  # put application's code here
    """
    首页
    :return:
    """
    # @app.route('/index')
    return render_template('index.html')

print(get_conf_section('REDIS', 'IP'))
app.config['SESSION_TYPE'] = 'redis'  # session存储格式为redis
app.config['SESSION_REDIS'] = Redis(  # redis的服务器参数
    host=get_conf_section('REDIS', 'IP'),  # 服务器地址
    port=int(get_conf_section('REDIS', 'PORT')))  # 服务器端口
app.config['SESSION_USE_SIGNER'] = True  # 是否强制加盐，混淆session
app.config['SECRET_KEY'] = os.urandom(24)  # 如果加盐，那么必须设置的安全码，盐
app.config['SESSION_PERMANENT'] = False  # sessons是否长期有效，false，则关闭浏览器，session失效
app.config['PERMANENT_SESSION_LIFETIME'] = 3600  # session长期有效，则设定session生命周期，整数秒，默认大概不到3小时。
Session(app)


@app.route('/n1', methods=['GET'])
def n1():
    session["k2"] = "admina"
    return "n1"


@app.route('/n2')
def n2():
    print(session["k2"])
    return "123"


@app.route('/login', methods=['GET'])
def login():
    cookie = '666666'
    headers = {'Cookie': cookie}
    return Response(jsonify({'message': 'Hello from Flask!'}), mimetype='application/json')


# from flask_session import Session
#
# # 定义一个 Session 对象，用于保存用户登录信息
# app.session_type = 'session'
# app.session = Session()


# @app.before_request
# def before_request():
#     # 获取当前时间
#     now = datetime.datetime.now()
#     # 计算 session 过期时间
#     expires = now + datetime.timedelta(days=30)
#     # 获取请求的 Session 信息
#     session_dict = request.cookies.to_dict()
#     # 验证 Session 是否有效
#     if not session.validate(session_dict, expires):
#         # 如果 Session 无效，返回 401 错误
#         return jsonify({'error': 'Session 无效', 'code': 401}), 401
#
#         # 获取请求的数据
#     cookies = request.cookies
#     cookie = cookies.get("Cookie", "")
#     # 进行效验
#     if not validate_request(cookie, None):
#         # 若效验不通过，返回错误信息
#         return jsonify({'error': '未登录'}), 400
#     # previous_route = request.full_path[1:]  # 获取路由信息
#     pass
#     # return jsonify({'message': 'Hello, world!'}), 200


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


# 蓝图导入
from src.chatgpt import urls as chatgpt

# 蓝图注册
app.register_blueprint(chatgpt.bp)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
