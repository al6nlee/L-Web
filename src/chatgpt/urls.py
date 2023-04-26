from flask import Blueprint

from src.chatgpt import views

# 创建蓝图
bp = Blueprint('chatgpt', __name__, url_prefix='/chatgpt')

# login
bp.add_url_rule(rule='/show_chatgpt', methods=["GET"], view_func=views.show_chatgpt, endpoint="show_chatgpt")
bp.add_url_rule(rule='/get_chatgpt_text', methods=["POST"], view_func=views.get_chatgpt_text,
                endpoint="get_chatgpt_text")
bp.add_url_rule(rule='/show_chatgpt_image', methods=["GET"], view_func=views.show_chatgpt_image,
                endpoint="show_chatgpt_image")
bp.add_url_rule(rule='/get_chatgpt_image', methods=["POST"], view_func=views.get_chatgpt_image,
                endpoint="get_chatgpt_image")
