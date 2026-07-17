class Solution(object):
    def sortedSquares(self, arr):
        a=[]
        b=[]
        n=len(arr)
        for i in range(0,n):
            if arr[i]>=0:
                a.append(arr[i])
            else:
                b.append(arr[i])
        
        if len(b)==0:
            for i in range(0,n):
                arr[i]=arr[i]*arr[i]
            return arr
        
        if len(a)==0:
            for i in range(0,n):
                arr[i]=arr[i]*arr[i]
            return arr[::-1]
        
        for i in range(0,len(a)):
            a[i]=a[i]*a[i] 
        
        for i in range(0,len(b)):
            b[i]=b[i]*b[i] 
            
        b.reverse()

        sort_arr=[]
        i=0
        j=0
        while i<len(a) and j<len(b):
            if a[i]>b[j]:
                sort_arr.append(b[j])
                j+=1
            else:
                sort_arr.append(a[i])
                i+=1

        while i<len(a):
            sort_arr.append(a[i])
            i+=1
        while j<len(b):
            sort_arr.append(b[j])
            j+=1

        return sort_arr
        
        