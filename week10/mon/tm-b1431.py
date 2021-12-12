import sys
input = sys.stdin.readline

def sum_digit(serial):
    result = 0
    for s in serial:
        if s.isdigit():
            result += int(s)
    return result

n = int(input())
serials = [input().strip() for _ in range(n)]

serials.sort(key = lambda x:(len(x),sum_digit(x), x))
for serial in serials:
    print(serial)