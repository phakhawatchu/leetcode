class Solution:
    def longestPalindrome(self, s: str) -> str:
        res_cnt = 0
        res_str = ""
        for i in range(len(s)):
            l,r = i,i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r-l+1 > res_cnt:
                    res_str = s[l:r+1]
                    res_cnt = len(res_str)
                l -= 1
                r += 1
            l,r = i,i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r-l+1 > res_cnt:
                    res_str = s[l:r+1]
                    res_cnt = len(res_str)
                l -= 1
                r += 1
        return res_str

if __name__ == '__main__':
    s = Solution()
    print(s.longestPalindrome("babad"))