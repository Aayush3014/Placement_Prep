# My Solution

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        lst = []
        sum = 0
        for i in nums:
            count = 0
            n = i
            while n>0:
                n = n//10
                count+=1
            lst.append(count)
        for j in lst:
            if j%2==0:
                sum+=1
        return sum
    
# Viewed Solution


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count1=0
        for i in nums: 
            if len(str(i))%2==0:
                count1+=1
        return count1