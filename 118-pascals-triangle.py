def generate(numRows: int) -> List[List[int]]:
    ans = [[1]]
    for i in range(2, numRows + 1):
        ans.append([1] + [ans[-1][j] + ans[-1][j + 1] for j in range(i - 2)] + [1])
    return ans

numRows = int(input("Enter number of rows: "))
print(generate(numRows))
