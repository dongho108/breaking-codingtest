import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())

visited = [False] * n
seq_list = [0] * m

def seq(n,m,depth):
    if depth == m :
        print(" ".join(map(str, seq_list)))
        return
    
    for i in range(n):
        if visited[i] == False:
            visited[i] = True
            seq_list[depth] = i+1
            seq(n, m, depth + 1)

            visited[i] = False

seq(n,m,0)