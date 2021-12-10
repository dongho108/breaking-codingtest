def solution(people, limit):
    people.sort()
    i, j = 0, len(people)-1
    cnt = 0
    while i <= j:
        if people[i] + people[j] <= limit:
            cnt += 1
            i += 1
            j -= 1
        else:
            cnt += 1
            j -= 1
    return cnt