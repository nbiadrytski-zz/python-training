from datetime import datetime

# importing object datetime from datetime library

delta = datetime.now() - datetime(1900, 12, 31)

print("Days from now to 1900 year:", delta.days)

print("Current time:", datetime.now())

print(datetime.strptime("2017-12-31", "%Y-%m-%d"))