class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left=0
        result=float('-inf')
        freq={}
        for right in range(len(s)):
            freq[s[right]]=freq.get(s[right],0)+1

            while len(freq)<right-left+1:
                freq[s[left]]-=1
                if freq[s[left]]==0:
                    del freq[s[left]]
                left+=1

            result=max(result,right-left+1)
        return 0 if result==float('-inf') else result
        