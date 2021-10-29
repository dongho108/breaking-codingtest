class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1 or len(s) == 1:
            return s

        zigzag = ["" for _ in range(numRows)]

        zigzag_index = 0
        zigzag_up = True
        for value in s:
            zigzag[zigzag_index] += value
            if zigzag_up :
                zigzag_index += 1
            else :
                zigzag_index -= 1

            if zigzag_index == numRows - 1 or zigzag_index == 0:
                zigzag_up = not(zigzag_up)
        
        return "".join(zigzag)

test = Solution()
print(test.convert(s = "PAYPALISHIRING", numRows = 3))
print(test.convert(s = "PAYPALISHIRING", numRows = 4))