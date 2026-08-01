class Solution:
    def defangIPaddr(self, address: str) -> str:
        '''ans=address.replace(".","[.]")
        return ans'''
        ans=""
        for i in address:
            if i==".":
                ans+="[.]"
            else:
                ans+=i
        return ans
        