def ls(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1

arr = [1,2,3,4,5,6,7,8]
target = 6

#arr = list(map(int, input("Enter numbers separated by space: ").split()))

result = ls(arr,target)
if result != -1:
    print("Element is found at index {result}".format(result = result))
else:
    print("Element not found")