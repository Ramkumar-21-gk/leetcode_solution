class Solution(object):
    def generateParenthesis(self, n):
            
        result = []

        def backtrack(current, opened, closed):
            if len(current) == 2 * n:
                result.append(current)
                return

            # We can add '(' while we still have opening parentheses left.
            if opened < n:
                backtrack(current + "(", opened + 1, closed)

            # We can add ')' only if it won't make the sequence invalid.
            if closed < opened:
                backtrack(current + ")", opened, closed + 1)

        backtrack("", 0, 0)
        return result