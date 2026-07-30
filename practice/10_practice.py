ages = {
    "철수": 21,
    "영희": 18,
    "민수": 30,
    "지수": 25,
    "수빈": 22
}


def count_even_age(age_dict):
    # 짝수 나이인 사람의 수를 반환하세요.
    count = 0

    for age in age_dict.values():
        if age % 2 == 0:
            count += 1

    return count

print(count_even_age(ages))   # 3