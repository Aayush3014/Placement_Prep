word = "abcdefd"
ch = "d"
count = word.count(ch)
str_list = word.split(ch)
empty_string = ch
for i in range(len(str_list[0])-1,-1,-1):
    empty_string += str_list[0][i]

# str_list[0] = empty_string
for i in range(1,len(str_list)):
    empty_string+=str_list[i]
    if empty_string.count(ch)==count:
        break
    else:    
        empty_string+=ch

print(str_list)
print(empty_string)


        if ch not in word:
            return word
        else:
            count = word.count(ch)
            str_list = word.split(ch)
            empty_string = ch
            for i in range(len(str_list[0])-1,-1,-1):
                empty_string += str_list[0][i]

            # str_list[0] = empty_string
            for i in range(1,len(str_list)):
                empty_string+=str_list[i]
                if empty_string.count(ch)==count:
                    break
                else:    
                    empty_string+=ch
            return empty_string