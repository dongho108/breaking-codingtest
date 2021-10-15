# 2X2 정사각형 확인
def square(graph):
    lst = []
    for x in range(4):
        for y in range(4):
            lst.append(graph[x][y]) # 기준
            lst.append(graph[x+1][y]) # 아래
            lst.append(graph[x][y+1]) # 오른쪽        
            lst.append(graph[x+1][y+1]) # 오른쪽 아래 대각선
            if lst.count('P') <= 1:
                lst = []
                continue
            if lst.count('P') == 2:
                if lst[0] == 'P':
                    if lst[1] == 'X' and lst[2] == 'X':
                        lst = []
                        continue
                if lst[1] == 'P':
                    if lst[0] == 'X' and lst[3] == 'X':
                        lst = []
                        continue
            return False
    return True

# 가로 3개 확인
def rectangle_v(graph):
    lst = []
    for x in range(5):
        for y in range(2):
            lst.append(graph[x][y]) # 기준
            lst.append(graph[x][y+1]) # 오른쪽        
            lst.append(graph[x][y+2]) # 오른쪽 오른쪽
            if lst.count('P') <= 1:
                lst = []
                continue
            if lst.count('P') == 2:
                if lst[1] == 'X':
                    lst = []
                    continue
            return False
    return True

# 세로 3개 확인
def rectangle_h(graph):
    lst = []
    for y in range(5):
        for x in range(2):
            lst.append(graph[x][y]) # 기준
            lst.append(graph[x+1][y]) # 아래        
            lst.append(graph[x+2][y]) # 아래 아래
            if lst.count('P') <= 1:
                lst = []
                continue
            if lst.count('P') == 2:
                if lst[1] == 'X':
                    lst = []
                    continue
            return False
    return True

def solution(places):
    new_places = []
    for i in range(5):
        temp = []
        for j in range(5):
            temp.append(list(places[i][j]))
        new_places.append(list(temp))
    
    answer = []
    for idx in range(5):
        graph = new_places[idx]
        if not square(graph):
            answer.append(0)
            continue
        if not rectangle_v(graph):
            answer.append(0)
            continue
        if not rectangle_h(graph):
            answer.append(0)
            continue
        answer.append(1)
    return answer