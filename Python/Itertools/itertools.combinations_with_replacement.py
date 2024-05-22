# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools
string, k = input().split(" ")
string = sorted(list(string))

result = itertools.combinations_with_replacement(string, int(k))
for x in result:
        print("".join(x))
