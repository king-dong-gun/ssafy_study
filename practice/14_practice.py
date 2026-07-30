scores = {
    "python": 95,
    "java": 72,
    "sql": 81,
    "algorithm": 60
}

def over_80(score_dict):
    count = 0
    for score in score_dict.values():
        if score >= 80:
            count += 1
    return count

print(over_80(scores))
# 2