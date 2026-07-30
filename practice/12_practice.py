user = {
    "name": "Kim"
}


def is_english_name(data):
    for name in data.values():
        first_char = name[0]

        if first_char.isalpha() and first_char.isascii():
            return True
        else:
            return False

print(is_english_name(user))   # True