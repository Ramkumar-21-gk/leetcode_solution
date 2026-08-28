
class Solution:
    def lexPalindromicPermutation(self, s, target):

        n = len(s)

        # Count characters
        count = [0] * 26

        for ch in s:
            count[ord(ch) - ord('a')] += 1

        # A palindrome can have at most one odd count
        odd = sum(c % 2 for c in count)

        if odd > 1:
            return ""

        # Find middle character
        middle = ""

        if n % 2 == 1:
            for i in range(26):
                if count[i] % 2 == 1:
                    middle = chr(i + ord('a'))
                    break

        # Characters available for LEFT half
        half = [c // 2 for c in count]

        half_len = n // 2

        prefix = []

        def can_make_greater():

            # Current prefix
            left = "".join(prefix)

            # Fill remaining characters with LARGEST possible chars
            for i in range(25, -1, -1):
                if half[i] > 0:
                    left += chr(i + ord('a')) * half[i]

            # Build palindrome
            palindrome = left + middle + left[::-1]

            return palindrome > target

        # Build left half
        for _ in range(half_len):

            found = False

            # Try smallest character first
            for i in range(26):

                if half[i] == 0:
                    continue

                # Choose this character
                half[i] -= 1
                prefix.append(chr(i + ord('a')))

                # Can this choice eventually produce
                # a palindrome > target?
                if can_make_greater():
                    found = True
                    break

                # Undo choice
                prefix.pop()
                half[i] += 1

            if not found:
                return ""

        # Construct final palindrome
        left = "".join(prefix)

        answer = left + middle + left[::-1]

        if answer > target:
            return answer

        return ""

