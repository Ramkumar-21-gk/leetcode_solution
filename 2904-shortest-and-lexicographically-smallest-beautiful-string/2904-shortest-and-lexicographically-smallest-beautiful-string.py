class Solution(object):
    def shortestBeautifulSubstring(self, s, k):
        ones = []

        for i, ch in enumerate(s):
            if ch == '1':
                ones.append(i)

        if len(ones) < k:
            return ""

        best = ""
        min_len = float('inf')

        for i in range(len(ones) - k + 1):
            start = ones[i]
            end = ones[i + k - 1]

            length = end - start + 1
            candidate = s[start:end + 1]

            if length < min_len:
                min_len = length
                best = candidate

            elif length == min_len:
                best = min(best, candidate)

        return best