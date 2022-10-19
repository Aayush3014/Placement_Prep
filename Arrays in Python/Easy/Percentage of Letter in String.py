class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        count = 0
        for i in range(len(s)):
            if s[i] == letter:
                count += 1
            result = (count*100)//len(s)
        return result