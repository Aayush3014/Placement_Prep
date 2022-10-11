
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