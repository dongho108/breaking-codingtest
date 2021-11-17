import sys


input = sys.stdin.readline
s = str(input())

open_check = False
stack = []
answer = ''
for i, x in enumerate(list(s)):
    if x == '\n':
        continue
    if x == '<':
        while stack:
            answer += stack.pop()
        open_check = True
    elif x == '>':
        open_check = False
    elif x == ' ':
        while stack:
            answer += stack.pop()
    else:
        if not open_check:
            stack.append(x)
            continue
    answer += x

while stack:
    answer += stack.pop()
print(answer)


# <asd><asd>abc def<ASD>abc<ASD>
# <asd>abc<asd>abc def<ASD>abc<ASD>
# abc def abc