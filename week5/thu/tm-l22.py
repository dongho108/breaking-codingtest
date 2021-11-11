class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []
        self.combinations(result,"",0,0,n)
        return result

        
    
    def combinations(self, result:list[str], s: str, open: int, close: int, max: int):
        if len(s) == max * 2:
            result.append(s)
            return
        
        if open < max:
            self.combinations(result, s + "(", open+1,close,max)
        
        if close < open:
            self.combinations(result, s + ")", open, close+1, max)


test = Solution()
print(test.generateParenthesis(1))