class Solution:
    def maxNumberOfFamilies(self, n, reservedSeats):
        rows = {}

        # Store reserved seats for each row
        for r, seat in reservedSeats:
            if r not in rows:
                rows[r] = set()
            rows[r].add(seat)

        # Initially every row can have 2 families
        ans = 2 * n

        for seats in rows.values():

            left = not any(seat in seats for seat in [2, 3, 4, 5])
            middle = not any(seat in seats for seat in [4, 5, 6, 7])
            right = not any(seat in seats for seat in [6, 7, 8, 9])

            # This row was counted as 2 initially
            if left and right:
                continue

            elif left or middle or right:
                # At least one group can fit
                ans -= 1

            else:
                # No group can fit
                ans -= 2

        return ans