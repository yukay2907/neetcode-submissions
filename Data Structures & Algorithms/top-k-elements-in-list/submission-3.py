from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        result=[]
        for num in nums:
            freq[num]+=1
        sorted_freq = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True)[:k])
        for key in sorted_freq.keys():
            result.append(key)
        return result
