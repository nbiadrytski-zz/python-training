import heapq
"""Sort and combine 2 already sorted lists"""
a = [1, 4, 7, 10]
b = [2, 5, 6, 11]

for x in heapq.merge(a, b):
    print(x)

# 1
# 2
# 4
# 5
# 6
# 7
# 10
# 11
