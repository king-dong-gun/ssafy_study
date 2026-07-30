user_data = {
    "email": "ssafy@naver.com"
}

def is_email_valid(data):
    email = data["email"]
    if "@" in email:
        return True
    else:
        return False

print(is_email_valid(user_data))
# True