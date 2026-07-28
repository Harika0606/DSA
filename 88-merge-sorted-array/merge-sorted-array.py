class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        lolo = []
        lol = sorted(nums1[:m] + nums2)
        for i in lol:
            lolo.append(i)
        for i in range(len(lolo)):
            nums1[i] = lolo[i]
        """
        Do not return anything, modify nums1 in-place instead.
        """

        