class Solution(object):
    def lengthOfLongestSubstring(self, s):
        low=0
        arr=list(s)
        n=len(arr)
        max_string=0
        freq={}
        for high in range(n):
            freq[arr[high]]=freq.get(arr[high],0)+1
            k=high-low+1
            if len(freq)<k:
                freq[arr[low]]-=1
                if freq[arr[low]]==0:
                    del freq[arr[low]]
                k=high-low+1   
                low+=1
            
            length=high-low+1
            max_string=max(length,max_string)
        return max_string