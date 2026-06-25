class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in range(len(asteroids)):
            alive = True
            while stack and asteroids[i] < 0 and stack[-1] > 0:
                if (-asteroids[i]) > stack[-1]:
                    stack.pop()
                elif (-asteroids[i]) == stack[-1]:
                    stack.pop()
                    alive = False
                    break
                else:
                    alive = False
                    break
            if alive:
                stack.append(asteroids[i])
            
        return stack