class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        answer = []
        alpha = [0 for _ in range(26)]
    
        for index in range(len(s)):
            alpha[ord(s[index]) - ord('a')] = index
            
        start, end = 0, 0
        for index in range(len(s)):
            end = max(alpha[ord(s[index]) - ord('a')], end)
            if index == end:
                answer.append(end - start + 1)
                start = index + 1
                
        return answer

print(Solution.partitionLabels(Solution,"eccbbbbdec"))