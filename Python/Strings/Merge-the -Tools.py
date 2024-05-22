def merge_the_tools(string, k):
    # your code goes here
    for i in range(0, len(string), k):
      items = set((" ".join(string[i:i+3]).split()))
      print("".join((items)))


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
