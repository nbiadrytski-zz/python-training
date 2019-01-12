a = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]


# remove duplicates from dict
def remove_duplicates(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


# from list a (list of dicts) remove absolutely duplicate dicts(where key-value match both)
b = list(remove_duplicates(a, key=lambda d: (d['x'], d['y'])))
print(b)  # [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 2, 'y': 4}]

# from list a (list of dicts) remove dicts where key[x] and its value are duplicated
c = list(remove_duplicates(a, key=lambda d: d['x']))
print(c)  # [{'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
