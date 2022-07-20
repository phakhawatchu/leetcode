class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1:
            return s
        else:
            row_str = [''] * numRows
            index, k = 0, 1
            for char in s:
                row_str[index] += char
                if index == (numRows - 1):
                    k = -1
                elif index == 0:
                    k = 1
                index += k
            return "".join(row_str)

if __name__ == '__main__':
    s = Solution()
    print(s.convert("PAYPALISHIRING", 3))