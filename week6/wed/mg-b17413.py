import sys
input = sys.stdin.readline


string = input().strip()
answer = ''
flipped = []
check = False
for temp in string:
    if temp == '<':
        if flipped:
            answer += ''.join(flipped)
            flipped = []
        answer += temp
        check = True
    elif check == True:
        answer += temp
        if temp == '>':
            check = False
    else:
        if temp == ' ':
            answer += ''.join(flipped)
            answer += temp
            flipped = []
        else:
            flipped.insert(0, temp)
if flipped:
    answer += ''.join(flipped)
print(answer)