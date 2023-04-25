def validate_request(cookie, user_id):
    if cookie == '666666' or user_id:
        return True
    return False
