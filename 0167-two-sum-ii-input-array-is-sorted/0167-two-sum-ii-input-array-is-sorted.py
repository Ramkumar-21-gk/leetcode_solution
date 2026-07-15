class Solution(object):
    def twoSum(self, numbers, target):
        i=0
        j=len(numbers)-1
        while i<=j:
            sum=numbers[i]+numbers[j]

            if target==sum:
                return [i+1,j+1]
            elif sum<target:
                i+=1
            else:
                j-=1
        return -1


obj=Solution()
obj.twoSum([2,7,11,15],9)