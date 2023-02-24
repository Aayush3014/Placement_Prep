class Solution:
    def repeatedCharacter(self, s: str) -> str:
        s1 = set()
        for i in range(len(s)):
            if s[i] in s1:
                return s[i]
            s1.add(s[i])