def kadanes_algorithm(arr):
    if not arr:
        return 0, []

    global_max = current_max = arr[0]
    start = end = s = 0

    for i in range(1, len(arr)):
        if arr[i] > current_max + arr[i]:
            current_max = arr[i]
            s = i
        else:
            current_max += arr[i]

        if current_max > global_max:
            global_max = current_max
            start = s
            end = i

    return global_max, arr[start:end + 1]


data1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(f"Max Subarray Sum for {data1}: {kadanes_algorithm(data1)}")

data2 = [1, 2, 3]
print(f"Max Subarray Sum for {data2}: {kadanes_algorithm(data2)}")

data3 = [-5, -2, -8, -1]
print(f"Max Subarray Sum for {data3}: {kadanes_algorithm(data3)}")