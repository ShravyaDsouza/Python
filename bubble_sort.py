def bubble_sort(arr):
    l = len(arr)-1

    for i in range(l):
        for j in range(0,l-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]


if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]

    bubble_sort(arr)

    print("Sorted array:")
    for i in range(len(arr)):
        print("%d" % arr[i], end=" ")