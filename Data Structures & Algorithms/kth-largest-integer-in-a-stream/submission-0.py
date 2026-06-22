class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.num = nums

    def add(self, val: int) -> int:
        self.num.append(val)
        self.num.sort()
        return self.num[len(self.num)-self.k]
