prices = [15000, 22000, 18000, 30000, 27000]


def count_expensive(price_list):
    # 코드를 작성하세요.
    # pass
    total = 0
    # 매개변수 price_list 쓰기
    for i in price_list:
        if i >= 20000:
            total += 1
    return total

print(count_expensive(prices)) # 3