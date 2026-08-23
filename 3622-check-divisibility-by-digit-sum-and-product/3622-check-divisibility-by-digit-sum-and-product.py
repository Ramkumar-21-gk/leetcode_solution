class Solution(object):
    def checkDivisibility(self, n):
        original_n = n
        digit_sum = 0
        digit_mul = 1

        while n > 0:
            digit = n % 10
            digit_sum += digit
            digit_mul *= digit
            n //= 10

        total_sum = digit_sum + digit_mul

        return original_n % total_sum == 0