import sys


input = sys.stdin.readline
n = int(input().strip())
serials = []
for i in range(n):
    serials.append(input().strip())


def sum_of_numbers(serial):
    result = 0
    for x in serial:
        if x.isdigit():
            result += int(x)
    return result


serials.sort(key=lambda x : (len(x),
                             sum_of_numbers(x),
                             x))

for serial in serials:
    print(serial)