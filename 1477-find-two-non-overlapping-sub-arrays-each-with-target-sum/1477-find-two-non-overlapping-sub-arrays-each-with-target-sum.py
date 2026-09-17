class Solution:
    def minSumOfLengths(self, arr, target):
        n = len(arr)

        # best[i] = minimum length of a valid subarray
        # completely inside arr[0...i]
        best = [float('inf')] * n

        left = 0
        curr_sum = 0
        ans = float('inf')

        for right in range(n):
            curr_sum += arr[right]

            while curr_sum > target:
                curr_sum -= arr[left]
                left += 1

            if curr_sum == target:
                length = right - left + 1

                # If there was a valid subarray before `left`,
                # combine it with current subarray.
                if left > 0 and best[left - 1] != float('inf'):
                    ans = min(ans, length + best[left - 1])

                # Store shortest valid subarray ending at or before right
                if right == 0:
                    best[right] = length
                else:
                    best[right] = min(best[right - 1], length)

            else:
                if right > 0:
                    best[right] = best[right - 1]

        return -1 if ans == float('inf') else ans