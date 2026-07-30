prices = [15000, 22000, 18000, 30000, 27000]


def count_expensive(price_list):
    count = 0

    # price_list를 반복하면서
    # 가격이 20000 이상인지 검사하고
    # 조건을 만족하면 count를 1 증가시키세요.
    for price in price_list:
        if price >= 20000:
            count += 1
    return count


print(count_expensive(prices))  # 3