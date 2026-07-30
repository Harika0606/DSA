class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[[]]
        for j in nums:
            n=len(ans)
            for i in range(n):
                ans.append(ans[i]+[j])
        return ans
        