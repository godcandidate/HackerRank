# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
s,k = input().split()

for x in range(1,int(k)+1):
    z = list(combinations(sorted(s),x))
    for i in z:
        print("".join(i))
