class Solution(object):
    def sumGame(self, num):
        n = len(num)
        half = n // 2

        diff = 0
        qdiff = 0

        for i in range(half):
            if num[i] == '?':
                qdiff += 1
            else:
                diff += int(num[i])

        for i in range(half, n):
            if num[i] == '?':
                qdiff -= 1
            else:
                diff -= int(num[i])

        # Odd difference in number of '?'
        if qdiff % 2 != 0:
            return True

        # Bob can win only when the differences can exactly cancel
        return 2 * diff != -9 * qdiff