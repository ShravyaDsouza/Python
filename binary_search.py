def bs(arr,target):
    l = 0
    h = len(arr)-1
    while l <= h:
        mid = (l+h)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            l = mid+1
        else:
            h = mid-1

    return -1

arr = [2, 5, 8, 12, 16, 23, 38, 56]
target = 16

result = bs(arr, target)
if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")
