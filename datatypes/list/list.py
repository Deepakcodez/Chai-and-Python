#List is like an array in other language
#List allow duplicate value

mylist = ["mango","grapes","peach","peach"]
list1 = ["abc", 34, True, 40, "male"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]



print(mylist)
print(mylist[0])
print(list1)




#The list() Constructor another way of defining list
list4 = list(( "mango", 4 , True))
print(list4)
print(type(list4))




#finding length of  list
print(len(mylist))  #4

#finding type of list
print(type(mylist))


#access desire values
print(mylist[:2])
print(mylist[2:3])


#Insert Items
mylist.insert(2,True)
print(mylist)

#append
mylist.append("appended item")
print(mylist)


# Extend list 
mylist.extend(list2)
print(mylist)


#remove
mylist.remove("peach")
print(mylist)

# remove specified index
mylist.pop(2)
del mylist[6]   #another method
print(mylist)



