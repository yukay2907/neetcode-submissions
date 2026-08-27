class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        res = []

        sortedByValue = dict(sorted(freq.items(), key = lambda item:item[1], reverse = True))

        for key,value in sortedByValue.items():
            if k == 0:
                break
            res.append(key)
            k -= 1
        return res