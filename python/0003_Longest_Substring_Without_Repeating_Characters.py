class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_str = {}
        cumulative = ""
        for val in s:
            if val in hash_str:
                try:
                    cumulative = cumulative[cumulative.index(val)+1:] + val
                except:
                    cumulative += val
                if (len(cumulative) > len(hash_str[val])):
                    hash_str[val] = cumulative
            else:
                cumulative += val
                hash_str[val] = cumulative
        if len(s) == 0:
            return 0
        return sorted([len(i) for i in hash_str.values()], reverse=True)[0]


if __name__ == '__main__':
    str = "pwwkew"
    s = Solution()
    print(s.lengthOfLongestSubstring(str))
    