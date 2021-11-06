def solution(s):
    answer = []
    ss = s + s

    first = ss[len(s)]
    i = len(s) - 1
    count = 0
    while i >= 0:
        if ss[i] == first:
            count += 1
        else:
            break
        i -= 1
    if count != 0:
        s = ss[len(s) - count: -count]

    first = s[0]
    count = 1
    for i in range(1, len(s)):
        if first != s[i]:
            answer.append(count)
            first = s[i]
            count = 1
        else:
            count += 1
    answer.append(count)
    return sorted(answer)


print(solution("abcdefaa"))
print(solution("abcdefg"))
# print(solution("aaaaaa"))
# print(solution("aaabbaaa"))
# print(solution("wowwow"))
