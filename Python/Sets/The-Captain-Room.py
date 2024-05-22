# Enter your code here. Read input from STDIN. Print output to STDOUT

k = input()
rooms = input().split()
single = set()
multiple = set()

for room in rooms: 
    single.add(room) if room not in single else multiple.add(room)

print(single.difference(multiple).pop())
