class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        lst = set()
        for i in range(len(words)):
            for j in range(len(words)):
                if words[i]!=words[j]:
                    if words[i] in words[j]:
                        lst.add(words[i])
                else:
                    pass
        return lst