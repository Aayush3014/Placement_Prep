class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        count = 0
        if word.isupper():
            return True
        elif word.islower():
            return True
        else:
            for i in word:
                if i.isupper():
                    count+=1
            if count == 1 and word[0].isupper():
                return True
            else:
                return False