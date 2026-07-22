class Solution(object):
    def characterReplacement(self, s, k):
        low,res=0,0
        n=len(s)
        f=[0]*256
        for high in range(n):
            f[ord(s[high])]+=1
            maxcount=max(f)
            leng=high-low+1
            diff=leng-maxcount

            while diff>k:
                f[ord(s[low])]-=1
                low+=1
                maxcount=max(f)
                leng=high-low+1
                diff=leng-maxcount
            
            leng=high-low+1
            res=max(res,leng)
        return res

        