prices = [12000, 35000, 18000, 27000, 9000]

def max_price(price_list):
    count = 0
    for price in price_list:
        if count < price:
            count = price
    return count

print(max_price(prices))
# 35000