# ! ----> set

# ? charctristics of set
# 1.) set can be kreated using {}
# 2.) the elements inside set are not indexed
# 3.) does not allow duplicate values
# 4.) it unordered
# 5.) heterogenous --> accept only unmutable datatypes
# 6.) mutable or changable

# *Eg:1
# s1 = {9, 9, 89, 7.76, 8+7j, (8,7,5), "truck", 'e'}
# print(s1)

# *Eg:2
# s2 = {5, 8, 98, [9,0]}
# print(s2) --> error

# *Eg;3
# min(), max(), len()

# *Eg
# ? to add element inside set

# s1 = {8, 78, 67, 'u'}
# add()
# s1.add(43)
# print(s1)

# update()
# s1.update([9,0])
# print(s1)

# ? T0 delete element inside set
#s1 = {8, 78, 67, 'u'}
# pop() # to delete one element randomly
# s1.pop()
# print(s1)

# remove()
# s1.remove(78)
# print(s1)

# discard()
# s1.remove(8967)
# print(s1)

# clear()
# l1 = {}
# print(tytpr(l1)) --> datatypr is dict

# s1 = set() # to create empty set
# print(type(s1))

# del(s1)
# print(s1)

# *join the sets
# s1 = {9, 0, 8}
# s2 = {9.90, "card", 't', 56}
# # union() --> to combine 2 sets
# s3 = s1.union(s2)
# print(s3)

# *intersections() --> to get common elements inside set
# s1 = {4, 5, 6}
# s2 = {5, 6, 7, 8}
# print(s1.intersection(s2))

# *difference()
# s1 = {4, 5, 6}
# s2 = {5, 6, 7, 8}
# print(s1.difference(s2))
# print(s2.difference(s1))
# print(s1.symmetric_difference(s2))

# isdijoint(),, issubset(), issuperset()
# s1 = {8, 9, 0}
# s2 = {6, 7, 5, 8, 9, 0}
# print(s1.issubset(s2))
# print(s2.issuperset(s1))

# ! ---> Problem:1
#s1 = {1,2,3,4,5}
#s2 = {3,2,7,8,9}

# for val in s1:
#    if val in s2:
#       str1 = "Its joint set"
# print(str1)
# ? o/p -->Its a joiset

# ! ---->dictionary
# Eg:1
# d1 = {1:100, 'a':200, 4.5:"hello"}
# print(d1)
# print(len(d1))

# ? char of dictionary
# 1.) have to be surrounded by ()
# 2.) It have to be in the form of key, value pair
# 3.) It is mutable
# 4.) duplicate keys are not allowed, duplicate values are allowed
# 5.) It is unindexed
# 6.) It is ordered
# 7.) Key does not allow mutable datatypes, values allow mutable datatype

# print(d1)
# or
# To access the values, have to use key
#print(d1[1]) # o/p 100

# ? some common functions
# len(), min, max()
# print(min(d1))
# print(max(d1))

# ? To find min, max based on values
# print(min(di.values()))
# print(max(d1.values()))

# ? dictionary based functions
# to add element (key and value pair) in dict
# d1 (1:100, 2:200, 3:300, 4:400)
# d1[5] = 500
# print(d1)

# ? To replace a value in dictionary
# d1 (1:100, 2:200, 3:300, 4:400)
# d1[2]="mango"
# print(d1)

# ? delete element from dictionary
# d1 (1:100, 2:200, 3:300, 4:400)
# popitem() # ---> to delete last key value pair in dict
# d1.popitem()
# print(d1)

#pop()
# d1.pop(2) #2 is the key in dictionary
# print(d1)

# clear(), del

# *join 2 dictionary
# update()
# d1 (1:100, 2:200, 3:300, 4:400)
# d2 ("a": "apple", "b": "boy", "g":"game"}
# d1.update(d2)
# print(d1)

# get() ---> used to get the value from a key
# d1 (1:100, 2:200, 3:300, 4:400)
# print(d1[90])
# print(dl.get(90))

# to print all the keys
# print(d1.keys())
# print(type(d1.keys()))

# to print all the values
# print(dl.values())


# *Iterating dictionary
# for val in d1: # to iterate keys alone 
#     print(val)
# for val in di.values(): # to iterate values alone
# print(val)

# to get both key and values
# for key, val in d1.items():
#    print(key, val)

# ! PROBLEM:1
# 1.) Swap elements in String list
# The original list is: ['Gfg', 'is', 'best', 'for', 'Geeks']
# List after performing character swaps: ['efg', 'is', 'bGst', 'for', 'eGGks']

n = int(input("Enter num of times"))
integer=[]
float_value = []
string=[]

for val in range(n):
    value = eval(input("Enter the values: "))
    if type(value)==int:
       integer.append(value)
    elif type(value) == float:
        float_value.append(value)
    elif type(value) == str:
        string.append(value)
    else:
        print("Pls provide data in int, float, string")
print(integer)
print(float_value)
print(string)










































































































































