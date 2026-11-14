class Solution:
    def sortedSquares(self, nums):
        arr_pos=[]
        arr_neg=[]
        for num in nums:
            if num>=0:
                arr_pos.append(num**2)
            else:
                arr_neg.append(num**2)

        arr_neg.sort()
        
        result=[]
        m=len(arr_pos)
        n=len(arr_neg)
        i,j=0,0
        while i<m and j<n:
            if arr_pos[i]<arr_neg[j]:
                result.append(arr_pos[i])
                i+=1
            else:
                result.append(arr_neg[j])
                j+=1

        while i<m:
            result.append(arr_pos[i])
            i+=1      
        while j<n:
            result.append(arr_neg[j])
            j+=1
        return result














        # negative = []
        # positive = []

        # # Separate negative and positive
        # for num in nums:
        #     if num < 0:
        #         negative.append(num * num)
        #     else:
        #         positive.append(num * num)

        # # Negative squares are in decreasing order
        # # so reverse them
        # negative.reverse()

        # # Now both are sorted
        # i = 0
        # j = 0

        # result = []

        # # Merge two sorted arrays
        # while i < len(negative) and j < len(positive):

        #     if negative[i] <= positive[j]:
        #         result.append(negative[i])
        #         i += 1
        #     else:
        #         result.append(positive[j])
        #         j += 1

        # # Remaining negative squares
        # while i < len(negative):
        #     result.append(negative[i])
        #     i += 1

        # # Remaining positive squares
        # while j < len(positive):
        #     result.append(positive[j])
        #     j += 1

        # return result