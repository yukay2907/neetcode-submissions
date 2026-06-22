class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last = m+n-1
        end1 = m-1
        end2 = n-1

        while end2>=0:
            if end1>=0 and nums1[end1]>nums2[end2]:
                nums1[last] = nums1[end1]
                end1 -=1
            else:
                nums1[last] = nums2[end2]
                end2 -=1
            last -=1