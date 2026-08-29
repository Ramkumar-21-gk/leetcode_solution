class Solution:
    def lexicographicallySmallestArray(self, nums, limit):
        n = len(nums)

        # Store value with original index
        arr = [(nums[i], i) for i in range(n)]

        # Sort by value
        arr.sort()

        result = nums[:]

        start = 0

        while start < n:
            end = start

            # Find all elements belonging to the same group
            while end + 1 < n and arr[end + 1][0] - arr[end][0] <= limit:
                end += 1

            # Get values and indices of this group
            values = []
            indices = []

            for i in range(start, end + 1):
                values.append(arr[i][0])
                indices.append(arr[i][1])

            # Put smallest values at smallest indices
            indices.sort()

            for i in range(len(values)):
                result[indices[i]] = values[i]

            start = end + 1

        return result