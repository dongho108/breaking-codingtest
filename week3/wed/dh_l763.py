class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        answer = []
        alpha = [0 for _ in range(26)]

        slist = list(s)
        for sl in enumerate(slist):
            alpha[ord(sl[1]) - ord('a')] = sl[0]

        start, end = 0, 0
        for sl in enumerate(slist):
            end = max(alpha[ord(sl[1]) - ord('a')], end)
            if sl[0] == end:
                answer.append(end - start + 1)
                print(end, start)
                start = end + 1
        return answer
