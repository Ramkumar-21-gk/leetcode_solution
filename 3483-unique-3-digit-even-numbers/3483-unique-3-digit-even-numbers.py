class Solution:
    def totalNumbers(self, digits):
        ans = set()

        n = len(digits)

        for i in range(n):          # hundreds
            if digits[i] == 0:
                continue

            for j in range(n):      # tens
                if j == i:
                    continue

                for k in range(n):  # units
                    if k == i or k == j:
                        continue

                    if digits[k] % 2 == 0:
                        num = digits[i] * 100 + digits[j] * 10 + digits[k]
                        ans.add(num)

        return len(ans)