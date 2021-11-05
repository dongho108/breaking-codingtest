def solution(word):
    alpha = ['A', 'E', 'I', 'O', 'U']
    words = []
    for i in range(5):
        s = alpha[i]
        words.append(s)
        for j in range(5):
            s += alpha[j]
            words.append(s)
            for k in range(5):
                s += alpha[k]
                words.append(s)
                for l in range(5):
                    s += alpha[l]
                    words.append(s)
                    for m in range(5):
                        s += alpha[m]
                        words.append(s)
                        s = s[:-1]
                    s = s[:-1]
                s = s[:-1]
            s = s[:-1]

    for i, w in enumerate(words):
        if word == w:
            return i + 1


print(solution("AAAAE"))
print(solution("AAAE"))
print(solution("I"))
print(solution("EIO"))