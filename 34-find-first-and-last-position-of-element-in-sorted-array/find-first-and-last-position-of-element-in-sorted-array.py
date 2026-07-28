class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lol=[]
        for i in range(len(nums)):
            if nums[i]==target:
                lol.append(i)
        if lol:
            return [lol[0],lol[-1]]
        else:
            return [-1,-1]
                
        