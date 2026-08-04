class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            lol= set()
            for j in range(i, len(s)):
                if s[j] in lol:
                    break
                lol.add(s[j])
                ans = max(ans, j - i + 1)

        return ans
        