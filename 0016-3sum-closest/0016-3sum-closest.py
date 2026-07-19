class Solution(object):
    def threeSumClosest(self, nums, target):
        arr = sorted(nums)
        n = len(arr)

        closest_sum = arr[0] + arr[1] + arr[2]

        for i in range(n - 2):

            left = i + 1
            right = n - 1

            while left < right:

                current_sum = arr[i] + arr[left] + arr[right]

                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum

                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    return current_sum

        return closest_sum