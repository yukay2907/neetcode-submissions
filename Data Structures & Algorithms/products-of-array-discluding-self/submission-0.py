class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            output=1
            ex=nums[:i]+ nums[i+1:]
            for j in range(len(ex)):
                output*=ex[j]
            result.append(output)
        return result