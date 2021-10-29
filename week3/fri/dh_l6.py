def convert(s, numRows):
    word = ['' for _ in range(numRows)]

    index = 0
    plus = 0
    for value in list(s):
        word[index] += value
        if numRows == 1:
            continue
        if index == 0:
            plus = 1
        elif index == numRows - 1:
            plus = -1
        index += plus
    answer = ''.join(word)
    return answer

print(convert("PAYPALISHIRING", 3))
print(convert("PAYPALISHIRING", 4))
print(convert("AB", 1))
print(convert("ABC", 1))