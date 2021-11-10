import sys
from itertools import combinations
input = sys.stdin.readline


def sol1(index, total):
    global count
    if index == N:
        return
    total += intList[index]
    if total == S:
        count += 1
    sol1(index + 1, total)
    sol1(index + 1, total - intList[index])

def sol2():
    count = 0
    for i in range(1, int(N)+1):
        for j in combinations(intList, i):
            if sum(j) == S:
                count += 1
    
    return count


if __name__ == "__main__":
    N, S = map(int, input().strip().split())
    intList = list(map(int, input().strip().split()))
    count = 0
    sol1(0, 0)
    print(count)
    
    count = sol2()
    print(count)