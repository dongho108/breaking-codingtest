def solution(n, wires):
    answer = 1e9
    
    tree = {}
    for edge in wires:
        if edge[0] in tree:
            tree[edge[0]].append(edge[1])
        else:
            tree[edge[0]] = [edge[1]]
        if edge[1] in tree:
            tree[edge[1]].append(edge[0])
        else:
            tree[edge[1]] = [edge[0]]
        
    for start1, start2 in wires:
        visited = [False] * (n+1)
        answer = min(answer, abs(bfs(tree, n, start1, start2) - bfs(tree, n, start2, start1)))
    return answer
        
def bfs(tree, n, start1, start2):
    cnt = 0
    visited = [False] * (n+1)
    queue = [start1]
    while queue:
        a = queue.pop()
        if a == start2:
            continue
        if not visited[a]:
            cnt += 1
            queue.extend(tree[a])
            visited[a] = True
    return cnt
