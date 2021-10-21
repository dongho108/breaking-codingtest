import sys

def find_meet(line1,line2):

    d = line1[0]*line2[1] - line1[1]*line2[0]
    if d == 0:
        return None
    
    x = line1[1]*line2[2] - line1[2]*line2[1]
    y = line1[2]*line2[0] - line1[0]*line2[2]
    return None if (x%d != 0) or (y%d != 0) else [x//d, y//d]

def solution(line):
    meets = []
    
    min_x, max_x = sys.maxsize, -sys.maxsize
    min_y, max_y = sys.maxsize, -sys.maxsize

    for i in range(len(line)-1):
        for j in range(i+1,len(line)):
            meet = find_meet(line[i],line[j])
            if meet != None:
                x,y = meet
                min_x = min(min_x, x)
                max_x = max(max_x, x)
                min_y = min(min_y, y)
                max_y = max(max_y, y)
                meets.append((x,y))
    
    graph = ['.'*(max_x-min_x+1)] * (max_y - min_y+1)

    for x, y in meets:
        x = x - min_x
        y = max_y - y
        
        target_line = list(graph[y])
        target_line[x] = '*'
        graph[y] = ''.join(target_line)

    return graph
print(solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]))