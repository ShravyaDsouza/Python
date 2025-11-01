def insertion_sort(arr):
    length = len(arr)
    for j in range(1, length):
        i = j-1
        key = arr[j]
        while i >= 0 and arr[i] > key:
            arr[i+1] = arr[i]
            i = i-1
        arr[i+1] = key

if __name__ == '__main__':
    arr = [64, 34, 25, 12, 22, 11, 90]

    insertion_sort(arr)

    print("Sorted array:")
    for i in range(len(arr)):
        print("%d" % arr[i], end=" ")