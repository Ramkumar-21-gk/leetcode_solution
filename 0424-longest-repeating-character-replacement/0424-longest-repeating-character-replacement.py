class Solution(object):
    def characterReplacement(self, s, k):
        freq=[0]*26
        low,res=0,0

        for high in range(len(s)):
            freq[ord(s[high])-ord('A')]+=1
            length=high-low+1
            max_freq=max(freq)
            diff=length-max_freq
            while diff>k:
                freq[ord(s[low]) - ord('A')] -= 1
                low += 1
                length=high-low+1
                max_freq=max(freq)
                diff=length-max_freq
                
            length=high-low+1
            res=max(res,length)
        return res