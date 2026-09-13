class Solution(object):
    def largestOverlap(self, img1, img2):
        n = len(img1)
        ans = 0

        for rowShift in range(-(n - 1), n):
            for colShift in range(-(n - 1), n):

                count = 0

                for i in range(n):
                    for j in range(n):

                        new_i = i + rowShift
                        new_j = j + colShift

                        if 0 <= new_i < n and 0 <= new_j < n:
                            if img1[i][j] == 1 and img2[new_i][new_j] == 1:
                                count += 1

                ans = max(ans, count)

        return ans