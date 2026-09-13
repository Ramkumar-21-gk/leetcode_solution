class Solution:
    def sortedSquares(self, nums):

        neg=[]
        pos=[]

        for num in nums:
            if num<0:
                neg.append(num*num)
            else:
                pos.append(num*num)
        
        neg.reverse()
        i,j=0,0
        result=[]
        while i<len(neg) and j<len(pos):
            if neg[i]<pos[j]:
                result.append(neg[i])
                i+=1
            else:
                result.append(pos[j])
                j+=1
        
        while i<len(neg):
            result.append(neg[i])
            i+=1

        while j<len(pos):
            result.append(pos[j])
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