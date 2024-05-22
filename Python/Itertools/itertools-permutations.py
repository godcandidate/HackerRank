# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import permutations

word , n = input().split()
mlist = sorted(list(permutations(word, int(n))))

for item in mlist:
  print("".join(item))
