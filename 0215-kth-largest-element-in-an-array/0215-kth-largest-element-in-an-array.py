import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        n=len(nums)
        heap=[]
        for i in range(0,k):
            heapq.heappush(heap,nums[i])
        
        for j in range(k,n):
            if nums[j]<=heap[0]:
                continue
            heapq.heappop(heap)
            heapq.heappush(heap,nums[j])

        return heap[0]
        