user_data = {
    "password": "python123"
}

def is_password_valid(data):
    password = data["password"]
    if len(password) > 8 :
        return True
    else:
        False

print(is_password_valid(user_data))
# True