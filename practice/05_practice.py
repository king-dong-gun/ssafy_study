scores = [85, 70, 92, 66, 78]


def min_score(score_list):
    # 첫 번째 점수를 최솟값으로 저장하세요.
    minimum = score_list[0]

    # score_list의 점수를 하나씩 반복하세요.
    # 현재 점수가 minimum보다 작으면
    # minimum을 현재 점수로 바꾸세요.

    for score in score_list:
        if score < minimum:
            minimum = score
    return minimum

print(min_score(scores))  # 66