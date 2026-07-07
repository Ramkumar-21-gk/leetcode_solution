class Solution(object):
    def isHappy(self, n):
        def sums(n):
            sum=0
            while n>0:
                d=n%10
                n=n//10
                sum=sum+d**2
            return sum
        slow=n
        fast=n
        while fast!=1:
            slow=sums(slow)
            fast=sums(fast)
            fast=sums(fast)

            if (slow==fast and slow!=1):
                return False
        return True