def solution(price, money, count):
    answer = 0
    for i in range(count):
        answer += (price * (i + 1))

    if answer > money:
        return answer - money
    else:
        return 0


print(solution(3, 20, 4))