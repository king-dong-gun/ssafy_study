scores = {
    "python": 90,
    "java": 85,
    "sql": 95
}


def total_score(score_dict):
    # 코드를 작성하세요.
    total = 0
    for scores in score_dict.values():
        # total = total + scores
        total += scores

    return total

print(total_score(scores)) # 270