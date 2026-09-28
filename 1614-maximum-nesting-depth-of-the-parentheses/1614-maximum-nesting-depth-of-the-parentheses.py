class Solution(object):
    def maxDepth(self, s):
        maxP = 0
        currentP = 0
        i = 0

        while i < len(s):

            if s[i] == "(":
                currentP = currentP + 1

                if maxP < currentP:
                    maxP = currentP

            elif s[i] == ")":
                currentP = currentP - 1

            i += 1

        return maxP