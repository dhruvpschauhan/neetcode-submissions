class Solution:
    def maxProfit(self, arr: List[int]) -> int:
        n=len(arr)
        buy=0
        maxpro=0
        for sell in range(1,n):
            if arr[sell]<arr[buy]:
                buy=sell
            else:
                profit=arr[sell]-arr[buy]
                maxpro=max(maxpro,profit)
        return maxpro