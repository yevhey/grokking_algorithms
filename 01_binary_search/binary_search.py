"""realization of binary search algorithm"""
def binary_search(sorted_arr, item):
    """finds position of element in array for log n"""
    low = 0
    high = len(sorted_arr) - 1

    while low <= high:
        mid = (low + high) / 2
        guess = sorted_arr[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

MY_LIST = [1, 3, 5, 7]

print binary_search(MY_LIST, 5)
print binary_search(MY_LIST, 6)
