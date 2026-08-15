class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lol=s.split()
        return len(lol[-1])