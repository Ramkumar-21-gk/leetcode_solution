class Solution:
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        from collections import Counter

        diff = [abs(a - b) for a, b in zip(nums1, nums2)]
        k = k1 + k2

        if sum(diff) <= k:
            return 0

        freq = Counter(diff)
        max_diff = max(diff)

        for d in range(max_diff, 0, -1):
            if freq[d] == 0:
                continue

            count = freq[d]
            need = min(k, count)

            # Reduce the largest differences by one
            if k >= count:
                freq[d - 1] += count
                k -= count
                freq[d] = 0
            else:
                freq[d] -= need
                freq[d - 1] += need
                k = 0
                break

            if k == 0:
                break

        return sum(d * d * count for d, count in freq.items())