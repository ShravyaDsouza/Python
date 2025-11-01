#1
largest = max(arr)
smallest = min(arr)

#2
largest = arr[0]
smallest = arr[0]

for num in arr:
    if num > largest:
        largest = num
    elif num < smallest:
        smallest = num

#3
arr.sort()
print("Smallest:", arr[0])
print("Largest:", arr[-1])