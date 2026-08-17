class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        myset = set()
        i=0
        while i<len(nums):
            if nums[i] in myset:
                return True
            myset.add(nums[i])
            i+=1
        return False