# Enter your code here. Read input from STDIN. Print output to STDOUT

N = int(input())


for _ in range(N):
    a = int(input())
    A = set(map(int,input().split()))
    b = int(input())
    B = set(map(int,input().split()))
    
    print(A.issubset(B))
    
