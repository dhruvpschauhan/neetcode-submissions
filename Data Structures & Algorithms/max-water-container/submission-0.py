class Solution:
    def maxArea(self, arr: List[int]) -> int:
        n=len(arr)
        left=0
        right=n-1
        maxi_area=0
        

        while left<right:
            
            height=min(arr[left],arr[right])
            width=right-left
            area=width*height
            
            maxi_area=max(maxi_area,area)

            if arr[left]<arr[right]:
                left+=1
            else:
                right-=1
        return maxi_area
            