class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        d = 0
        lst = []
        for i in num:
            d = d*10+i
        k = str(k + d)
        # final_num = str(final_num)
        for i in range(len(k)):
            lst.append(int(k[i]))
        return lst