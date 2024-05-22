# Enter your code here. Read input from STDIN. Print output to STDOUT

m = int(input())
a = set(input().split())

n = int(input())
b = set(input().split())

result = sorted(a.symmetric_difference(b), key = int)
print ("\n".join(result))
