import sys
input = sys.stdin.readline


if __name__ == "__main__":
    N, L = map(int, input().strip().split())
    water = sorted(list(map(int, input().strip().split())))

    if L == 1:
        print(N)
    
    else:
        tape = 0
        result = 0
        for i in range(N):
            if water[i] > tape:
                tape = water[i] + L - 1
                result += 1
        
        print(result)

