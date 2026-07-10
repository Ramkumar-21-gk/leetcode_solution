class Solution(object):
    def removeDuplicates(self, s):
        arr=list(s)
        stack=[]
        for i in range(0,len(arr)):
            if len(stack)==0 :
                stack.append(arr[i])
            elif arr[i]==stack[-1]:
                stack.pop()
            else:
                stack.append(arr[i])

        return "".join(stack)