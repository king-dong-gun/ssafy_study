user_data = {
    "id": "ssafy7"
}


def is_valid_id(data):
    # data에서 id 값을 꺼내세요.
    # 아이디의 마지막 글자를 확인하세요.
    # 마지막 글자가 숫자이면 True
    # 숫자가 아니면 False를 반환하세요.

    # 마지막 숫자를 가져와야함
    # isdigit: 숫자인지 문자열인지 판별하는 함수
    if data["id"][-1].isdigit():
        return True
    else:
        return False

print(is_valid_id(user_data))  # True