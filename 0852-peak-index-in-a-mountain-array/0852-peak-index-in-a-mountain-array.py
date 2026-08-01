class Solution(object):
    def peakIndexInMountainArray(self, arr):
        low=0
        high=len(arr)-1
        res=-1
        while(low<=high):
            mid=(low+high)//2
            if arr[low]<arr[low+1]:
                low=low+1
            else:
                res=mid
                high=mid-1
        return res       