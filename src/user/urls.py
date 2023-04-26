from flask import Blueprint

from src.user import session_redis

# 创建蓝图
bp = Blueprint('效验session', __name__, url_prefix='/user')

# login
bp.add_url_rule(rule='/login', methods=["GET"], view_func=session_redis.login, endpoint="login")
bp.add_url_rule(rule='/check_session', methods=["GET"], view_func=session_redis.check_session, endpoint="check_session")
bp.add_url_rule(rule='/logout', methods=["GET"], view_func=session_redis.logout, endpoint="logout")

# redis
