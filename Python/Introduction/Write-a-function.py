def is_leap(year):
    if (year % 100 == 0 or year % 400 == 0):
        return False
    if (year % 4 == 0):
        return True
    return False

year = int(input())
print(is_leap(year))
