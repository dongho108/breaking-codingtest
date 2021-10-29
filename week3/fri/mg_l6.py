class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if numRows == 1 or numRows >= len(s):
            return s

        row = [''] * numRows
        index, step = 0, 0

        for item in s:
            row[index] += item
            if index == 0:
                step = 1
            elif index == numRows-1:
                step = -1
            index += step

        return ''.join(row)