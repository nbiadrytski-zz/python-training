a = [1, 5, 2, 1, 9, 1, 5, 10]


# remove duplicates from list, but preserve order
def list_with_unique_values(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


b = list(list_with_unique_values(a))
print(b)