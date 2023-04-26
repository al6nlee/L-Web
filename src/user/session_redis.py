# 登录
def login():
    """
    帐号 username test
    密码 password test001
    :return:
    """

    username = request.json.get("username")
    password = request.json.get("password")
    if not all([username, password]):
        return jsonify(msg="参数不完整")
    if username == "test" and password == "test001":
        # 如果通过，保存登录状态在session中
        session["username"] = username
        return jsonify(msg="登录成功！")
    else:
        return jsonify(msg="帐号或者密码错误")


# 检查登录状态
def check_session():
    username = session.get("username")
    print(session)
    if username is not None:
        return jsonify(username=username)
    else:
        return jsonify(msg="出错了，没登录")


# 退出
def logout():
    session.clear()
    return jsonify(msg="退出成功")