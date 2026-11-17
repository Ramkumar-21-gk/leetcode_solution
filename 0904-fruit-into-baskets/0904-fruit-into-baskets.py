class Solution(object):
    def totalFruit(self, fruits):
        freq={}
        left=0
        result=float('-inf')

        for right in range(len(fruits)):
            freq[fruits[right]]=freq.get(fruits[right],0)+1

            while len(freq)>2:
                freq[fruits[left]]-=1
                if freq[fruits[left]]==0:
                    del freq[fruits[left]]
                left+=1

            result=max(result,right-left+1)
            
        return result