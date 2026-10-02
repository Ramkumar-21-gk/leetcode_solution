class Solution(object):
    def isPalindrome(self, s):
        s = s.lower()
        arr = []

        for char in s:
            value = ord(char)

            if ('a' <= char <= 'z') or ('0' <= char <= '9'):
                arr.append(char)

        left = 0
        right = len(arr) - 1

        while left < right:
            if arr[left] != arr[right]:
                return False

            left += 1
            right -= 1

        return True