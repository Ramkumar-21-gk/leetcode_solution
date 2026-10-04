class Solution(object):
    def threeSum(self, nums):
        result = []
        nums.sort()

        for i in range(len(nums) - 2):

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            target = -1 * nums[i]

            while left < right:

                sums = nums[left] + nums[right]

                if sums == target:
                    result.append([nums[left], nums[right], nums[i]])

                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif sums > target:
                    right -= 1

                else:
                    left += 1

        return result
