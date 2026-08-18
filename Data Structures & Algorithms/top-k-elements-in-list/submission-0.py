class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq_map = {}

        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1

        result = sorted(freq_map, key=lambda x: freq_map[x], reverse=True)
        return result[0:k]