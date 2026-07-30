scores = [85, 90, 77, 100, 68]


def even_sum(score_list):
    # 코드를 작성하세요.
    # pass
    total = 0
    for i in scores:
        if i % 2 == 0:
            total += i
    return total

print(even_sum(scores)) # 258