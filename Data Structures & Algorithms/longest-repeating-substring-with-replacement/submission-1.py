class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap = dict()
        left=0
        n=len(s)
        maxsub=0
        for right in range(n):
            # add to hashmap
            hashmap[s[right]]=hashmap.get(s[right],0)+1
            #replacement need calculate
            rep_need=(right-left+1)-max(hashmap.values())
            #make sure window is valid
            if rep_need>k:
                hashmap[s[left]]=hashmap[s[left]]-1
                left+=1
            #calculate window size after each step
            maxsub=max(maxsub,right-left+1)
        return maxsub