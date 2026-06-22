class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = []
        one = []
        two = []
        ans = []
        for num in nums:
            if num == 0:
                zero.append(num)
            elif num == 1 :
                one.append(num)
            elif num == 2:
                two.append(num)
        
        ans.extend(zero)
        ans.extend(one)
        ans.extend(two)

        nums.clear()
        nums.extend(ans)