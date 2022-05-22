def sum_array(arr):
    if not arr:
        return 0
    return arr[0] + sum_array(arr[1:])

list = [20, 30, 2, 4, 100]
print(sum_array(list))