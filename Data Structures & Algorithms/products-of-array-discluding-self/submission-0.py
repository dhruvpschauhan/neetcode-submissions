class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=1
        answer = []
        i=0
        for num in nums:
            answer.append(prefix)
            prefix*=num
            i+=1
        suffix=1
        for i in range(len(nums)-1,-1,-1):
            answer[i]*=suffix
            suffix*=nums[i]


        return answer