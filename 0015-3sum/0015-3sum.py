class Solution(object):
    def threeSum(self,nums):
        arr = sorted(nums)
        n = len(arr)
        ans = []

        for i in range(n):

            if i > 0 and arr[i] == arr[i-1]:
                continue

            target = -arr[i]

            left = i + 1
            right = n - 1

            while left < right:

                s = arr[left] + arr[right]

                if s == target:

                    ans.append([arr[i], arr[left], arr[right]])

                    left += 1
                    right -= 1

                    while left < right and arr[left] == arr[left-1]:
                        left += 1

                    while left < right and arr[right] == arr[right+1]:
                        right -= 1

                elif s < target:
                    left += 1

                else:
                    right -= 1

        return ans


# print(threeSum([-1, 0, 1, 2, -1, -4]))
            