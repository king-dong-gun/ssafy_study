user_data = {
    "id": "ssafy",
    "password": "python123"
}


def is_valid_user(data):
    # data에서 id 값을 꺼내세요.
    # data에서 password 값을 꺼내세요.
    #
    # id 또는 password가 빈 문자열이면 False
    # 그렇지 않으면 True를 반환하세요.
    if data["id"] == "" or data["password"] == "":
        return False
    else:
        return True

print(is_valid_user(user_data))  # True