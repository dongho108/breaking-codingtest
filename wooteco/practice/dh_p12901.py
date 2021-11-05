def solution(a, b):
    calendar = {
        1 : 31, 2 : 29, 3 : 31, 4 : 30, 5 : 31, 6 : 30, 7: 31, 8 : 31, 9 : 30, 10 : 31, 11 : 30, 12 : 31}
    week = {0: "FRI", 1: "SAT", 2: "SUN", 3: "MON", 4: "TUE", 5: "WED", 6: "THU"}

    day = 0
    for i in range(a - 1):
        day += calendar[i + 1]
    day += b

    return week[day % 7 - 1]

print(solution(5, 24))
print(solution(10, 12))