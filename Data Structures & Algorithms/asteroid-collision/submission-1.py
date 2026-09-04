class Solution:
    def asteroidCollision(self, ass: List[int]) -> List[int]:
        stack=[]
        for num in ass:
            while stack and stack[-1]>0 and num<0:
                if -num>stack[-1]:
                    stack.pop()
                elif -num==stack[-1]:
                    stack.pop()
                    break
                else:
                    break
            else:
                stack.append(num)
        return stack