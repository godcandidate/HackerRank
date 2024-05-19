if __name__ == '__main__':
    n = int(input())
    lis = (map(int, input().split()))
    mlist = list(lis)
    
    maxi = 0
    runner_up = 0
    
    for score in mlist:
        if score > maxi:
            runner_up = maxi
            maxi = score
        elif score > runner_up and score != maxi:
            runner_up = score
    print(runner_up)
