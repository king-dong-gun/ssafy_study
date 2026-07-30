# 입력
# 3
# 3 17 1 39 8 41 2 32 99 2
# 22 8 5 123 7 2 63 7 3 46
# 6 63 2 3 58 76 21 33 8 1   

# 출력
#1 24
#2 29
#3 27

# 테스트 케이스 개수
T = int(input())

# 테스트 케이스 개수 만큼 반복
for test_case in range(1, T + 1):
    nums = list(map(int, input().split()))
    total = sum(nums)
    avg = (total + 5) // 10
    print(f"#{test_case} {avg}")
