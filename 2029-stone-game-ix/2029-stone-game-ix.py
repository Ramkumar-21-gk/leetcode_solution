class Solution(object):
    def stoneGameIX(self, stones):

            c = [0, 0, 0]

            for x in stones:
                c[x % 3] += 1

            c0, c1, c2 = c

            if c1 == 0 and c2 == 0:
                return False

            if c0 % 2 == 0:
                return c1 > 0 and c2 > 0

            return abs(c1 - c2) > 2