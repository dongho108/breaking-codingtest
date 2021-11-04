def divide(p):
    checker = True
    u = ""
    v = ""
    count = 0
    for i in p:
        if checker:
            u += i
        else:
            v += i
        if i == "(":
            count +=1
        else:
            count -= 1
        if count == 0:
            checker = False
    return u,v

def checker(u):
    count = 0
    checker = True
    for i in u:
        if i == "(":
            count += 1
        else:
            count -= 1
        if count < 0:
            checker = False
            break
    if count != 0:
        checker = False
    return checker

def make(p):
    u,v = divide(p)
    result = ""
    if checker(u):
        result += u
        if v:
            result += make(v)
        return result
        
    else:
        result = "("
        result += make(v)
        result += ")"
        for i in u[1:-1]:
            if i == "(":
                result += ")"
            else:
                result += "("
        return result

def solution(p):
    answer = ''
    if p == "":
        return answer
    
    return make(p)