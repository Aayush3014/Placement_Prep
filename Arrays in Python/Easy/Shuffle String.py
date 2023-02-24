class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        lst = [""]*len(s)
        for i, j in enumerate(indices):
            lst[j] = s[i]
        return "".join(lst)