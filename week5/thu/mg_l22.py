class Solution:
    from itertools import combinations
    
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []
        parentheses = [''] * (n*2)
        parentheses[0], parentheses[-1] = '(', ')'
        for item in list(combinations(range(n*2-2), n-1)):
            temp = parentheses.copy()
            for j in range(n-1):
                temp[item[j]+1] = '('
            check, left, right = True, 0, 0
            for k in range(len(temp)):
                if temp[k] == '(':
                    left += 1
                if left <= right:
                    check = False
                    break
                if temp[k] == '':
                    temp[k] = ')'
                    right += 1
            if check == False:
                continue
            answer.append(''.join(temp))
        return answer