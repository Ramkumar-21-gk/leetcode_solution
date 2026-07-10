class Solution(object):
    def removeDuplicates(self, s):
        arr=list(s)
        stack=[]
        uni=arr[0]
        stack.append(uni)

        for i in range(1,len(arr)):
            if len(stack)==0:
                stack.append(arr[i])
            elif arr[i]==stack[-1]:
                stack.pop()
            else:
                stack.append(arr[i])

        return "".join(stack)