class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = -1
        r = len(nums)
        while l+1 < r:
            mid = l + (r-l)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid
            else:
                r = mid
        return -1