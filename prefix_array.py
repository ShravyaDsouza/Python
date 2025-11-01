def create_prefix_sum_array(arr):
    n = len(arr)
    prefix_sum = [0] * n

    if n > 0:
        prefix_sum[0] = arr[0]

    for i in range(1, n):
        prefix_sum[i] = prefix_sum[i-1] + arr[i]

    return prefix_sum


A = [10, 20, 30, 40, 50]
P = create_prefix_sum_array(A)
print(f"Original Array A: {A}")
print(f"Prefix Sum Array P: {P}")