def quick_sort(arr):
    _quicksort(arr, 0, len(arr) - 1)
    return arr


def _quicksort(arr, low, high):
    if low < high:
        pi = _partition(arr, low, high)

        _quicksort(arr, low, pi - 1)
        _quicksort(arr, pi + 1, high)


def _partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


data = [10, 7, 8, 9, 1, 5]
print(f"Original List: {data}")
sorted_data = quick_sort(data)
print(f"Sorted List: {sorted_data}")