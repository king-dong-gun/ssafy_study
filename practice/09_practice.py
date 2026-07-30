scores = [75, 88, 91, 67, 99]


def max_score(score_list):
    # 가장 큰 점수를 반환하세요.
    maxium = score_list[0]
    for score in score_list:
        if score > maxium:
            maxium = score
    return maxium

print(max_score(scores))   # 99