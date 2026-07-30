# 입력
# 3
# 3 17 1 39 8 41 2 32 99 2
# 22 8 5 123 7 2 63 7 3 46
# 6 63 2 3 58 76 21 33 8 1

# 출력
# 1 200
# 2 208
# 3 121

# 테스트 케이스 개수
T = int(input())

# 테스트 케이스 개수 만큼 반복
for test_case in range(1, T + 1):
    numbers = list(map(int, input().split()))
    total = 0

    for number in numbers:
        if number % 2 == 1:
            total += number

    print(f"#{test_case} {total}")
