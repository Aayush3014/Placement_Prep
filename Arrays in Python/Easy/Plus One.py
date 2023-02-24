class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        d = 0
        lst = []
        for i in digits:
            d = d*10+i
        d = str(d+1)
        for i in range(len(d)):
            lst.append(int(d[i]))
        return lst
