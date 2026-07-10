class Solution(object):
    def minEatingSpeed(self, piles, h):
        def find(piles,n,speed):
            h=0
            for i in range(0,n):
                h=h+piles[i]//speed

                if piles[i]%speed!=0:
                    h+=1
            return h
        
        n=len(piles)
        low=1
        high=0
        for i in range(0,n):
            if high<piles[i]:
                high=piles[i]

        while(low<=high):
            guess=(low+high)//2
            eat_hour=find(piles,n,guess)

            if (eat_hour>h):
                low=guess+1
            else:
                res=guess
                high=guess-1
        return res