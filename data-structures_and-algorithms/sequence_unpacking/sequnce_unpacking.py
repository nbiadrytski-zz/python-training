# Any sequence (or iterable) can be unpacked into variables using a simple assignment operation
p = (4, 5)
x, y = p

print(x)  # 4
print(y)  # 5
print("1-------------------------------------------------------------")

data = ['ACME', 50, 91.1, (2012, 12, 21)]
name, quantity, price, date = data
print(name)  # ACME
print(quantity)  # 50
print(price)  # 91.1
print(date)  # (2012, 12, 21)
print("2-------------------------------------------------------------")

# When unpacking, you may sometimes want to discard certain values
# you can often just pick a throwaway variable name for it
data2 = ['ACME', 50, 91.1, (2012, 12, 21)]
_, shares, price2, _ = data2
print(shares)  # 50
print(price2)  # 91
print("3-------------------------------------------------------------")

