from flask import Blueprint

from src.index import views


# 创建蓝图
bp = Blueprint('index', __name__, url_prefix='/index')

# zml-批量更新权限状态
bp.add_url_rule(rule='/', methods=["GET"], view_func=views.index, endpoint="")
