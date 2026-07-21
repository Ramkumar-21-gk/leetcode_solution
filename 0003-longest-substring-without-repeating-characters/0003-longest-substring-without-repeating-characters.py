class Solution(object):
    def lengthOfLongestSubstring(self, s):
        low,res=0,0
        freq={}
        for high in range(len(s)):
            freq[s[high]]=freq.get(s[high],0)+1

            while freq[s[high]]>1:
                freq[s[low]]-=1
                low+=1
            leng=high-low+1
            res=max(res,leng)

        return res
        