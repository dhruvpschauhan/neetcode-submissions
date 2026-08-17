class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        myset = set(nums)
        max_streak=0
        for num in myset:

            if num-1 not in myset:
                current_num = num
                current_streak=1

                while current_num+1 in myset:
                    current_streak+=1
                    current_num+=1
                max_streak=max(current_streak,max_streak)
        return max_streak