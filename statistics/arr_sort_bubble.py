def bubble_sort(arr):
    arr_length = len(arr) - 1
    for i in range(arr_length):
        for j in range(arr_length - i):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


ls = [2, 1, 5, 4, 3]
print(bubble_sort(ls))