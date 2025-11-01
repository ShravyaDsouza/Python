m = [[1, 2, 3],
     [4, 5, 6]]

n = [[1, 2, 3],
     [4, 5, 6]]

if len(m[0]) != len(n):
    print("Matrix multiplication not possible.")
else:
    result = [[0 for _ in range(len(n[0]))] for _ in range(len(m))]

    for i in range(len(m)):
        for j in range(len(n[0])):
            for k in range(len(n)):
                result[i][j] += m[i][k] * n[k][j]

    print("Resultant Matrix:")
    for row in result:
        print(row)
