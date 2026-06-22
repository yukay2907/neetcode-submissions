class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        check = []
        for ast in asteroids:
            while check and ast < 0 and check[-1] > 0:
                diff = ast + check[-1]
                if diff < 0:
                    check.pop()
                elif diff > 0:
                    ast =0
                else:
                    ast = 0
                    check.pop()
            if ast:
                check.append(ast)
        return check