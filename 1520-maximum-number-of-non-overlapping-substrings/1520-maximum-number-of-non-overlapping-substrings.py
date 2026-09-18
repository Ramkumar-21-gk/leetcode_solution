class Solution:
    def maxNumOfSubstrings(self, s):
        n = len(s)

        # Store first and last occurrence of each character
        first = [n] * 26
        last = [-1] * 26

        for i, ch in enumerate(s):
            idx = ord(ch) - ord('a')
            first[idx] = min(first[idx], i)
            last[idx] = i

        intervals = []

        # Find the smallest valid interval for each character
        for c in range(26):
            if last[c] == -1:
                continue

            left = first[c]
            right = last[c]
            valid = True

            i = left

            while i <= right:
                idx = ord(s[i]) - ord('a')

                # Character appears before our interval
                if first[idx] < left:
                    valid = False
                    break

                # Expand interval
                right = max(right, last[idx])

                i += 1

            if valid:
                intervals.append((left, right))

        # Choose intervals that finish earliest
        intervals.sort(key=lambda x: x[1])

        ans = []
        prev_end = -1

        for left, right in intervals:
            if left > prev_end:
                ans.append(s[left:right + 1])
                prev_end = right

        return ans