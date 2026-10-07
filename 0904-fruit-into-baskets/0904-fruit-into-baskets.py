class Solution(object):
    def totalFruit(self, fruits):
        low=0
        freq={}
        n=len(fruits)
        k=2
        max_fruits=0
        for high in range(n):
            freq[fruits[high]]=freq.get(fruits[high],0)+1

            while len(freq)>k:
                freq[fruits[low]]-=1
                if freq[fruits[low]]==0:
                    del freq[fruits[low]]
                low+=1

            length=high-low+1

            max_fruits=max(length,max_fruits)

        return max_fruits