user_data = {
    "name": "김싸피",
    "age": 24
}


def is_adult(data):
    # 코드를 작성하세요.
    if data["age"] >= 20:
        return True
    else:
        return False

print(is_adult(user_data)) # True