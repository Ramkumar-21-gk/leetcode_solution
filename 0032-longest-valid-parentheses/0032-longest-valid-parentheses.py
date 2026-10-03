class Solution(object):
    def longestValidParentheses(self, s):
        stack = [-1]
        longest = 0

        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            else:
                stack.pop()

                if not stack:
                    # This ')' cannot be matched, so it becomes the new boundary.
                    stack.append(i)
                else:
                    longest = max(longest, i - stack[-1])

        return longest
            