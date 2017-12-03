"""selection sort implemention"""
def find_smallest(arr):
    """finds smallest element in given array"""
    smallest_index = 0
    smallest = arr[smallest_index]
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selection_sort(arr):
    """sorts array by selection sort"""
    new_arr = []
    new_arr_len = len(new_arr)
    while new_arr_len < len(arr):
        smallest = find_smallest(arr)
        new_arr.append(arr[smallest])
        arr.pop(smallest)
    return new_arr

print selection_sort([3, 5, 2, 7, 6, 9, 3])
