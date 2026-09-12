from bisect import bisect_right

class Solution:
    def maximumWeight(self, intervals):
        n = len(intervals)

        # Add original index
        intervals = [
            [start, end, weight, i]
            for i, (start, end, weight) in enumerate(intervals)
        ]

        # Sort by starting time
        intervals.sort()

        # Store all starting times
        starts = [interval[0] for interval in intervals]

        # next[i] = first interval whose start > intervals[i][1]
        next_index = [0] * n

        for i in range(n):
            next_index[i] = bisect_right(
                starts,
                intervals[i][1]
            )

        # dp[i][k] = best answer from i onward
        # when we can still select k intervals
        dp = {}

        def solve(i, k):
            if i == n or k == 0:
                return (0, [])

            if (i, k) in dp:
                return dp[(i, k)]

            # Option 1: Skip current interval
            skip_score, skip_indices = solve(i + 1, k)

            # Option 2: Take current interval
            take_score, take_indices = solve(
                next_index[i],
                k - 1
            )

            take_score += intervals[i][2]
            take_indices = [
                intervals[i][3]
            ] + take_indices

            # Choose better score
            if take_score > skip_score:
                ans = (take_score, take_indices)

            elif take_score < skip_score:
                ans = (skip_score, skip_indices)

            else:
                # Same score → lexicographically smaller indices
                take_sorted = sorted(take_indices)
                skip_sorted = sorted(skip_indices)

                if take_sorted < skip_sorted:
                    ans = (take_score, take_indices)
                else:
                    ans = (skip_score, skip_indices)

            dp[(i, k)] = ans
            return ans

        score, answer = solve(0, 4)

        return sorted(answer)