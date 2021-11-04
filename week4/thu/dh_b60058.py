def is_right(p):
    stack = []
    for x in p:
        if x == '(':
            stack.append(x)
        elif x == ')':
            if stack:
                top = stack.pop()
                if top != '(':
                    return False
            else:
                return False
    return True


def my_reverse(lst):
    for i in range(len(lst)):
        if lst[i] == '(':
            lst[i] = ')'
        else:
            lst[i] = '('


def set_right(u, v):
    if is_right(u):
        return u

    u = list(u)
    u.pop(0)
    if u:
        u.pop(-1)

    new = '(' + v + ')'
    if u:
        my_reverse(u)
        new += ''.join(u)
    return new


def separator(p):
    left_cnt = 0
    right_cnt = 0

    inx = 0
    for i in range(len(p)):
        if p[i] == '(':
            left_cnt += 1
        else:
            right_cnt += 1
        if left_cnt != 0 and left_cnt == right_cnt:
            inx = i
            break
    return p[:inx + 1], p[inx + 1:]


def solution(p):
    if p == "" or is_right(p):
        return p

    u, v = separator(p)

    if is_right(u):
        return u + solution(v)
    else:
        return set_right(u, solution(v))


print(solution(")("))
print(solution("(()())()"))
print(solution("()))((()"))