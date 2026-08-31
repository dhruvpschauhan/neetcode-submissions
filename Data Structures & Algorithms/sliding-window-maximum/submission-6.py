from collections import deque

class Solution:
    def maxSlidingWindow(self, arr: List[int], k: int) -> List[int]:
        left=0
        dq = deque()
        answers=[]
        
        for right in range(len(arr)):
            if right-left+1>k:
                left+=1
            while dq and dq[0]<left:
                dq.popleft()
            while dq and arr[dq[-1]]<arr[right]:
                dq.pop()

            

            dq.append(right)

            
            if right-left+1==k:
                answers.append(arr[dq[0]])
        return answers