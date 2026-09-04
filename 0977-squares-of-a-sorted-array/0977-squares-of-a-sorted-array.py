class Solution:
    def sortedSquares(self, nums):

        negative = []
        positive = []

        # Separate negative and positive
        for num in nums:
            if num < 0:
                negative.append(num * num)
            else:
                positive.append(num * num)

        # Negative squares are in decreasing order
        # so reverse them
        negative.reverse()

        # Now both are sorted
        i = 0
        j = 0

        result = []

        # Merge two sorted arrays
        while i < len(negative) and j < len(positive):

            if negative[i] <= positive[j]:
                result.append(negative[i])
                i += 1
            else:
                result.append(positive[j])
                j += 1

        # Remaining negative squares
        while i < len(negative):
            result.append(negative[i])
            i += 1

        # Remaining positive squares
        while j < len(positive):
            result.append(positive[j])
            j += 1

        return result