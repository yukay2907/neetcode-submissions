class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        check=0
        for i in range (len(nums)):
            current = nums[i]
            rest = nums[:i] + nums[i+1:]
            for j in rest:
                if current == j:
                    check=1
                    return True
        if check == 0:
            return False