class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ang = {}
        for str in strs:
            sorted_str = sorted(str)
            srted = "".join(sorted_str)
            if srted not in ang:
                ang[srted] = []

            ang[srted].append(str)

        return list(ang.values())

