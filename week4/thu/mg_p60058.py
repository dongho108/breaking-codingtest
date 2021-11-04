def split_uv(string):
    left, right = 0, 0
    for i in range(len(string)):
        if string[i] == '(':
            left += 1
        if string[i] == ')':
            right += 1
        if left == right:
            u = string[0:i+1]
            v = string[i+1:]
            return u, v

def check(u):
    stack = []
    for i in u:
        if i == '(':
            stack.append(i)
        else:
            if len(stack) == 0:
                return False
            if stack[-1] == '(':
                stack.pop()
    if len(stack) == 0:
        return True
    else:
        return False

def solution(p):
    answer = ''
    
    if len(p) == 0:
        return p

    u, v = split_uv(p)
    chk = check(u)
    
    if chk == True:
        return u + solution(v)
    if chk == False:
        answer += '('
        answer += solution(v)
        answer += ')'
        for i in u[1:-1]:
            if i == '(':
                answer += ')'
            elif i == ')':
                answer += '('
    return answer