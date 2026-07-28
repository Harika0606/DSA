class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans=[]
        sortii=sorted(p)
        for i in range(len(s)-len(p)+1):
            substr=s[i:i+len(p)]     
            if sorted(substr)==sortii:
                ans.append(i)
        return ans
        