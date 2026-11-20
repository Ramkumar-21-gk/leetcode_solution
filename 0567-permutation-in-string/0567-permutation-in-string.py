
class Solution:
    def checkInclusion(self, s1, s2):

        if len(s1) > len(s2):
            return False

        count1 = [0] * 26
        count2 = [0] * 26

        # Count characters in s1 and first window of s2
        for i in range(len(s1)):
            count1[ord(s1[i]) - ord('a')] += 1
            count2[ord(s2[i]) - ord('a')] += 1

        # Check first window
        if count1 == count2:
            return True

        # Sliding window
        for right in range(len(s1), len(s2)):

            # Add new character
            count2[ord(s2[right]) - ord('a')] += 1

            # Remove character leaving the window
            left = right - len(s1)
            count2[ord(s2[left]) - ord('a')] -= 1

            if count1 == count2:
                return True

        return False
