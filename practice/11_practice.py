user = {
    "email": "ssafy@naver.com"
}


def is_valid_email(data):
    for email in data.values():
        if "@" in email:
            return True

    return False

print(is_valid_email(user))   # True