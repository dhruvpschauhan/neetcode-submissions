class Solution:
    def search(self, arr: List[int], target: int) -> int:
        low=0
        high=len(arr)-1
        while low<=high:
            mid=(low+high)//2
            #target found at mid
            if arr[mid]==target:
                return mid

            #if arr is left sorted
            if arr[mid]>arr[high]:
                if arr[low]<=target<=arr[mid]:
                    high=mid-1
                else:
                    low=mid+1

            # if arr is right sorted
            else:
                if arr[mid]<=target<=arr[high]:
                    low=mid+1
                else:
                    high=mid-1
        return -1
                
