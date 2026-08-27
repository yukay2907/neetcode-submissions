class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(numbers)):
            rem = target - numbers[i]
            if rem in hashmap:
                return [hashmap[rem],i+1]
            hashmap[numbers[i]] = i+1
        