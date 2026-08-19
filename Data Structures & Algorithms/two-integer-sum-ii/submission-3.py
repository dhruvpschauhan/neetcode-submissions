class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap = dict()
        for i in range(0,len(numbers)):
            if target-numbers[i] in hashmap:
                return [hashmap[target-numbers[i]]+1,i+1]
            hashmap[numbers[i]]=i