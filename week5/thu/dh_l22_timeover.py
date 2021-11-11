from itertools import permutations


def is_right_par(par):
    st = []
    for p in par:
        if p == '(':
            st.append(p)
            continue
        else:
            if not st:
                return False
            if st.pop() != '(':
                return False
    return True


def solution(n):
    answer = []
    data = ['('] * n + [')'] * n
    pars = list(set(list(permutations(data, n * 2))))
    for par in pars:
        if is_right_par(par):
            answer.append(''.join(par))
    return sorted(answer)


print(solution(3))