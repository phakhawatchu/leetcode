class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        numbers = ['0','1','2','3','4','5','6','7','8','9']
        signs = ["+", "-"]
        sign = ""
        while i < len(s) and s[i] == ' ':
            i += 1
        if len(s) != i:
            if s[i] in signs:
                sign = s[i]
                i += 1
            if len(s) == i:
                return 0
            else:
                num_str = ""
                for char in s[i:]:
                    if char in numbers:
                        if (char == '0') and (len(num_str) == 0):
                            pass
                        else:
                            num_str += char
                    else:
                        break
                if num_str == "":
                    return 0
                else:
                    res = int(sign + num_str)
                    res = res if res > -2**31 else -2**31
                    res = res if res < 2**31 - 1 else 2**31 - 1
                    return res
        else:
            return 0

if __name__ == '__main__':
    s = Solution()
    print(s.myAtoi("42"))