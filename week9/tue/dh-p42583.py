def solution(bridge_length, weight, truck_weights):
    answer = 0
    arrive = []
    ing = []
    wait = [x for x in truck_weights]

    while len(arrive) != len(truck_weights):
        answer += 1
        ing_weight = 0
        pop_cnt = 0
        for i in range(len(ing)):
            ing[i][1] += 1
            if ing[i][1] == bridge_length:
                arrive.append(ing[0][0])
                pop_cnt += 1
            else:
                ing_weight += ing[i][0]
        while pop_cnt > 0:
            ing.pop(0)
            pop_cnt -= 1
        if wait:
            if ing_weight + wait[0] <= weight and len(ing) < bridge_length:
                ing.append([wait.pop(0), 0])
    return answer


print(solution(2, 10, [7,4,5,6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))