class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i=0
        hashmap = dict()
        while i<len(nums):
            if target-nums[i] in hashmap:
                return [hashmap[target-nums[i]],i]
            hashmap[nums[i]] = i
            i+=1
