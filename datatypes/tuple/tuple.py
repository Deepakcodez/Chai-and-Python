# tuple is like a list but it cant be change

tup = (3,4,5,"mango", "cherry")
notAtuple = ("mango")  # this will acts as a int 
#coorect syntax is  ("mango",)

print(tup)
print(tup[0])

#length
print(len(tup))

#type
print(type(tup))

#create tupple by constructor
tup2 = tuple(("mango","banana"))
print(tup2)

#access tuple
print(tup[0])   #3
print(tup[-1])  #cherry
print(tup[2:3])


# Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called. But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.

fruits = ("mango","kiwi");  # cant change
print(fruits)

changeIntoList = list(fruits)  # change tuple into list

changeIntoList[0] = "changedFruit"

fruits =  tuple(changeIntoList)
print(fruits)


#join tuple
joinedtup = tup + fruits
print(joinedtup)


