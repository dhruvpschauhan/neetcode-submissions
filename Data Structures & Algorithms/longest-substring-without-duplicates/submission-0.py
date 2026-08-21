class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = dict()
        left=0
        maxsub=0
        n=len(s)
        for right in range(n):
            hashmap[s[right]]=hashmap.get(s[right],0)+1

            while hashmap[s[right]]>1:
                hashmap[s[left]]-=1
                
                if hashmap[s[left]]==0:
                    del hashmap[s[left]]
                left+=1
            maxsub=max(maxsub,right-left+1)
        return maxsub