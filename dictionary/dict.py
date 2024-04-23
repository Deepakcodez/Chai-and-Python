# When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change.

dict = {
    "name" : "Deepak",
    "course" : "Btech",
    "phone" : 87548935,
    "friend" : ["abhi","muskan","nimmo"]
}
print(dict)
print(dict["name"])
print(dict.get("course"))

#dict keys
print(dict.keys())

#dict values
print(dict.values())


#1 for in  loop on dict
for values in dict:
     print(values,":", dict[values])

#2 For in Loop
for keys, values in dict.items():
     print( keys ," : ", values)



#update  also use for create new item
dict["name"] = "karan"
print(dict)
dict.update({"name":"Deepak"})
print(dict)
    


#Delete 
dict.pop("phone")    
print(dict)

dict.popitem()  # pop last inserted item
print(dict)


#delete
del dict        #this will delete whole dict you cant even print
print(dict)     #give error