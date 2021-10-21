def solution(line):
    # 교점 구하기
    intersection = set()
    min_x, max_x, min_y, max_y = 1e11, -1e11, 1e11, -1e11
    for i in range(len(line)-1):
        for j in range(i+1, len(line)):
            # AD-BC != 0
            if line[i][0]*line[j][1] - line[i][1]*line[j][0] != 0:
                x = (line[i][1]*line[j][2]-line[i][2]*line[j][1])/(line[i][0]*line[j][1]-line[i][1]*line[j][0])
                y = (line[i][2]*line[j][0]-line[i][0]*line[j][2])/(line[i][0]*line[j][1]-line[i][1]*line[j][0])
                if x==int(x) and y==int(y):
                    intersection.add((int(x), int(y)))
                    if int(x) < min_x:
                        min_x = int(x)
                    if int(x) > max_x:
                        max_x = int(x)
                    if int(y) < min_y:
                        min_y = int(y)
                    if int(y) > max_y:
                        max_y = int(y)
    # print(intersection)
    # print(min_x, max_x, min_y, max_y)
    
    # 점 찍기
    answer = []
    for _ in range(max_y-min_y+1):
        temp = '.'*(max_x-min_x+1)
        answer.append(temp)
    
    # 별 찍기
    for star in intersection:
        answer[max_y-star[1]] = answer[max_y-star[1]][0:star[0]-min_x] + '*' + answer[max_y-star[1]][star[0]-min_x+1:]
            
    return answer