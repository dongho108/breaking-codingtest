num = int(input())

def solution(num):
    if num == 1:
        return 0
    if num == 2 or num == 3:
        return 1
    d = [0] * (num + 1)
    d[1], d[2], d[3] = 1, 1, 1
    for i in range(4, num+1):
        if i % 2 == 0 and i % 3 == 0:
            d[i] = min(d[i-1], d[int(i/2)], d[int(i/3)]) + 1
        elif i % 2 == 0:
            d[i] = min(d[i-1], d[int(i/2)]) + 1
        elif i % 3 == 0:
            d[i] = min(d[i-1], d[int(i/3)]) + 1
        else:
            d[i] = d[i-1] + 1
    return d[-1]

print(solution(num))