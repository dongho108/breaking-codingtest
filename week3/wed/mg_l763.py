class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        answer = []
        string = list(s)
        temp = []
        while string:
            check = string.pop(0)
            temp.append(check)
            for item in set(temp):
                if item in string:
                    break
            else:
                answer.append(len(temp))
                temp = []
        return answer