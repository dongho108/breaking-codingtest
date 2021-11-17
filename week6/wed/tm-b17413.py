import sys

input = sys.stdin.readline


if __name__ == "__main__":
    S = input().strip()
    
    tag_check = False
    result = ""
    word = ""
    for s in S:
        if s == "<":
            result += word[::-1]
            tag_check = True
            word = ""
        if tag_check:
            word += s
            if s == ">":
                result += word
                tag_check = False
                word = ""
        else:
            if s.isalnum():
                word += s
            else:
                result += word[::-1] + " "
                word = ""
    
    if word:
        result += word[::-1]
    
    print(result)