class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev = 0
        temp = x
        while temp > 0:
            digit = temp % 10
            rev = rev*10 + digit
            temp = temp // 10
        return rev == x

if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome(121))
                    