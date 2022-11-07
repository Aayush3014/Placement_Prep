class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        hash = set()
        for i in arr:
            if i*2 in hash or (i/2 in hash):
                return True
            else:
                hash.add(i)
        return False

