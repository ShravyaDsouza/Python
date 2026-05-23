t = int(input())

for _ in range(t):
    n = int(input())
    for i in range(n+1, 2*n+1):
        print(i,end=" ")
    print()

"""
Claus -> 1<=ai<=2*n and adjacent elements and their sum are distinct 
"""