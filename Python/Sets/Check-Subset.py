# Enter your code here. Read input from STDIN. Print output to STDOUT

N = int(input())


for _ in range(N):
    a = int(input())
    A = set(input().strip())
    b = int(input())
    B = set(input().strip())
    
    print(A.issubset(B))
