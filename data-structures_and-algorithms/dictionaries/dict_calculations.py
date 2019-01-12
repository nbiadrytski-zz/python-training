prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75,
    'TEST': 999.9
}

# find min price and its company name
min_price = min(zip(prices.values(), prices.keys()))
print(min_price)

# find max price and its company name
max_price = max(zip(prices.values(), prices.keys()))
print(max_price)

# sort rices and its company name
prices_sorted = sorted(zip(prices.values(), prices.keys()))
print(prices_sorted)

# which company has lowest price? apply key function
lowest_company_price = min(prices, key=lambda k: prices[k])
print(lowest_company_price)  # FB

# which company has lowest price? apply key function
highest_company_price = max(prices, key=lambda k: prices[k])
print(highest_company_price)  # TEST

# get min value without company
min_value = prices[min(prices, key=lambda k: prices[k])]
print(min_value)  # 10.75