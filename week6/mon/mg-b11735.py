import sys
input = sys.stdin.readline

n, q = map(int, input().split())
Rnums, Rnums_sum, Rnums_cnt = [], 0, 0
Cnums, Cnums_sum, Cnums_cnt = [], 0, 0

sum_ = sum(range(1, n+1))
for i in range(q):
    direction, num = input().split()
    total = int(num)*n + sum_
    if direction == 'R':
        if int(num) in Rnums:
            print(0)
            continue
        print(total - Cnums_sum - Cnums_cnt*int(num))
        Rnums.append(int(num))
        Rnums_sum += int(num)
        Rnums_cnt += 1
    elif direction == 'C':
        if int(num) in Cnums:
            print(0)
            continue
        print(total - Rnums_sum - Rnums_cnt*int(num))
        Cnums.append(int(num))
        Cnums_sum += int(num)
        Cnums_cnt += 1