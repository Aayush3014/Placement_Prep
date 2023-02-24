# Default Solution
total = "abcdefghijklmnopqrstuvwxyz"
sentence = "leetcode"
sentence_list = []
for i in range(len(sentence)):
    sentence_list.append(sentence[i])
for j in range(len(total)):
    if total[j] in sentence_list:
        print(True)
        break
    else:
        print(False)
        break
# print(sentence_list)


# Optimized Solutions

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
		# if any alphabet has 0 count in sentence, we return False and True othewise.
        alpha = "abcdefghijklmnopqrstuvwxyz"
        for al in alpha:
            if sentence.count(al)==0:
                return False
        return True
