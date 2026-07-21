class Solution(object):
    def totalFruit(self, fruits):
        low,res=0,0
        k=2
        freq={}
        for high in range(len(fruits)):
            freq[fruits[high]]=freq.get(fruits[high],0)+1

            while len(freq)>k:
                freq[fruits[low]]-=1
                if freq[fruits[low]] == 0:
                    del freq[fruits[low]]
                low+=1
            
            leng=high-low+1
            res=max(res,leng)
        return res
