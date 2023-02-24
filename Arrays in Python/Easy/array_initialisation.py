from array import array

vals = array('i',[5,8,9,7,4,0])   # Initializing a new array.

newArr = array(vals.typecode,(a for a in vals))   # Creating a new array from old array.


# Iterating using for loop 

# for i in newArr:
#     print(i,end=' ')


# Iterating using for loop 
i = 0
while i<len(newArr):
    print(newArr[i])
    i+=1