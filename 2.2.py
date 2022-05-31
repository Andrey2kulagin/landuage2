fullprice_arr = [99, 199, 299, 399, 499]
for full_price in fullprice_arr:
    prices_str = {}
    discount_price = round(full_price * 60 / 100, 2)
    discount = round(full_price - discount_price, 2)
    prices_str["Цена со скидкой: "] = discount_price
    prices_str["Полная цена: "] = full_price
    prices_str["Сумма скидки:"] = discount
    print(prices_str)

