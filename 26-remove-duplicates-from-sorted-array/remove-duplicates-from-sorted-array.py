class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        dup = []
        ayo = []
        for i in nums:
            if i not in dup:
                dup.append(i)
            else:
                ayo.append('_')
        final = dup + ayo
        nums[:] = final
        return len(dup)