n = int(input())
s = set(map(int, input().split()))

N = int(input())

for i in range(N):
    opt = input().split()
    
    if opt[0] == "pop":
        s.pop()
    elif opt[0] == "remove":
        s.remove(int(opt[1]))
    elif opt[0] == "discard":
        s.discard(int(opt[1]))
print(sum(s))

    
    
