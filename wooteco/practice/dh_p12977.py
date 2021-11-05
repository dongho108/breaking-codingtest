from itertools import combinations


def is_prime(x):
    i = 2
    while i * i <= x:
        if x % i == 0:
            return False
        i += 1
    return True


def solution(nums):
    answer = 0
    comb_list = list(combinations(nums, 3))
    for comb in comb_list:
        if is_prime(sum(comb)):
            answer += 1

    return answer


print(solution([1,2,3,4]))
print(solution([1,2,7,6,4]))
print(solution([1, 2, 3, 4, 5]))