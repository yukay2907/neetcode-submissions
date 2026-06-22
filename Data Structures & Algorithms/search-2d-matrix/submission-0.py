class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flattened = [item for row in matrix for item in row]
        l = 0
        r = len(flattened)-1
        while l<=r:
            mid = l + (r-l)//2

            if flattened[mid] == target:
                return True
            
            elif flattened[mid] < target:
                l = mid + 1
            
            else:
                r = mid - 1
        
        return False