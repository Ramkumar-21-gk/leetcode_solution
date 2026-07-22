class Solution(object):
    def characterReplacement(self, s, k):
        low = 0
        res = 0
        f = [0] * 256

        for high in range(len(s)):
            f[ord(s[high])] += 1

            while (high - low + 1) - max(f) > k:
                f[ord(s[low])] -= 1
                low += 1

            res = max(res, high - low + 1)

        return res
# class Solution(object):
#     def characterReplacement(self, s, k):
#         low,res=0,0
#         n=len(s)
#         f=[0]*256
#         for high in range(n):
#             f[ord(s[high])]+=1
#             maxcount=max(f)
#             leng=high-low+1
#             diff=leng-maxcount

#             while diff>k:
#                 f[ord(s[low])]-=1
#                 low+=1
#                 maxcount=max(f)
#                 leng=high-low+1
#                 diff=leng-maxcount
            
#             leng=high-low+1
#             res=max(res,leng)
#         return res

        