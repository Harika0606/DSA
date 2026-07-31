class Solution:
    def reverseWords(self, s: str) -> str:
        ans=[]
        text=s.split()
        for i in text:
            ans.append(i[::-1])
        return " ".join(ans)      