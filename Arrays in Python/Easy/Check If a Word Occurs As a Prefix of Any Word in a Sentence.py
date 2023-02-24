sentence = "i love eating burger"
searchWord = "burg"
word_list = sentence.split(" ")
for i in word_list:
    if i.startswith(searchWord):
        print(word_list.index(i)+1)
print(word_list)