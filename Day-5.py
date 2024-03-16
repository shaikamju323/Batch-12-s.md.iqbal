#! To insert ot add element inside list

#append() --> used to add elelement at last position of list
#11 = [9, 8, 0, 6]
#11.append("car")
# print(11)

#n = int(input("enter the number of inputs: "))
#for i in range(0, n):
#  a, b = list(map(int, input().split()))
#  print(a, b)

# ! -----> common functions for list

#l1 = [6,7,8,9,0]
# print(len(l1))

# print(max(l1))
# print(min(l1))

# l1 = [6, 8, 9, "p", "u"]
# print(max(l1)) #--> error coz its a combination of list and string
#  print(min(l1)) # --> error coz its a combination of list and string

#11 [6, 7, 8, 9, 0, 8.89, -5, 0.78]
#print(min(l1)) # -5

# l1 [6, 7, 8, 9, 0, 8.89, -5, 0.78]
# index() --> to get index value of specific element
# print(l1.index(9))

# l1 = [6,6,6, 7, 8, 9, 0,18.89, -5, 0.78]
# count() --> how many num of times an element is repeated
# print(11.count(6))

# ! some functions which is specifically used for list

# To add element inside list
# ? insert(index_value, element) --> to add element at specific index position
# l1 = [6,6,6, 7, 8, 9, 0, 8.89, -5, 0.78]
# *pop() ---> last element will be deleted
# 11.pop()
# print(11)

# *pop(index_value)  --> used to delete element at specific index
# 11.pop(4) #4 is index value
# print(l1)


# *remove(element) --> used to delete element directly 
# l1.remove(8.89)
# print(l1)

# clear() --> to complete delete all element in list
# l1.clear()
# print(l1)

# del --> to delete the list
# del 11 #or del (11)
# print(11)

# ? > join 2 lists

# l1 = [9, 0, 8]
# l2 = ["p", "o", "t", 34]
# print(11+12)

# ! or

# *extend() --> to combine 2 1ists
# 11.extend(12)
# print(11)

# ? --> copy()
# l1 = [6, 7, 8, 9, 3]
# 12 = 11.copy()
# print(12)
# print(11)

# print(id(11))
# print(id(12))


# ! diff between shallow copy and deep copy

# *shallow copy
# import copy
# l1 = [8, 9, 8, [5, 6], [3, 2, 1]]
# l2 copy.copy(11)
# l1.appen (890)
# print(11)
# print(12)

# *deep copy --> used to copy the list with nested list
# import copy
# l1 = [8, 9, 0, [5, 6], [3, 2, 1]]
# print(11[-1][1]) --> to index nested list

# 12 = copy.copy (11)
# 11[-1].append('cars')
# print(11)
# print(12)

# ? sort --> arrange elelemts in list in ascending or descending order
# 11 [9, 7, 45,0,-6, 5, 12]
# # 11.sort() # to arrange in ascending order
# # print(11)

# 11.sort(reverse=True) # to sort in descending order
# print(11)

# 11 ['z', 'i', 'o', 'p', '9']
# 11.sort()
# print(l1) # --> error

# list constructor
# list() to conver other collection datatype to list
# l3 = ((8, 9, 0))
# print(list(l3))

#14 (8, 9)
#print(list(14))

# ! ---> nested list

# l1 = [8, 9, [0, 8, 7], ["p", "o", 'y'], [8, 't']]
# print(11[-2][1]) # --> 0

# print(11[1:4])
# print(11[1:-1])

# ? to delete "t" from 11
# l1[-1].remove('t')
# print(l1)

# ? combine these ["p", "o",'y'], [8, 't'] lists in 11 to ["p", "o", 'y', 8, 't']
# l1[-2].extend(l1[-1])
# 11.pop(-1)
# print(11)


# !-------> Tuple
# char of tuple
# 1.) Tuple have to be surrounded by ()
# 2.) The elements inside tuple are not changable
# 3.) The elements inside tuple are indexed
# 4.) The element will execute in order
# 5.) It is heterogenous
# 6.) It allow duplicate elements

# eg:
# t1 = (8, 8, 9, 6, 5.78, [9, 0], (6, 8), "hey", 9+6j)
# print(tl)
# print(type(t1))

# ? indexing, slicing are all same as list

# l1 = (8)
# print(type(l1)) # int
# 11 = (8)
# print(type(l1)) # tuple

# t1 = 8,9
# print(type(t1)) # tuple

# t2 = 8,
# print(type(t2))  # tuple

# len(),min(),max(),index(),count() --> all same as list

# to add element inside tuple --> cannot add
# cannot delete any element from tuple

# *join 2 tuples
# t1 = (8, 9, 8)
# t2 = (6, 7, 8)
# print(t1+t2)


# *To add all element inside list and tuple
# sum()
# 11 = (8, 9, 7, 6)
# print(sum(11))

# *sort tuple
 #t1 =(8, 9, 0,89,12)
# print(tuple(sorted(t1)))
# print(tuple(sorted(t1, reverse=True)))

# * Iterate list and tuples

# * Itereate based on elements
# l1 = [9, 8, 0, 6, 5]
# for i in 11
# print(i)

#Iterate based on index value
#11 = [9, 8, 0, 6, 5, 8, 56]
#for i in range(0,len(11):
#print(l1(i))

# *join the strings
# s1 = "hello"
# s2 = 'world'
# print(s1+s2)

# s1 = '''how are you
# iam fine
# hey there
# '''
## *splilines()--> used to split the string based on lines
# print(s1.splitlines())

# *find()--> Find the index based on a charachter
# s1 "hello world"
# print(s1.find('z'))
# print(s1.index('z'))

# * join() -->
#l1 ["hey", "there"]
#print(" ".join(l1))
#print("$".join(l1))

# s1 = "Welcome to all"
# print(s1.endswith('1'))
# print(sl.startswith('W'))

# s1 = "67"
# print(type(s1))
# print(s1.isdigit())

# *Print the string in reverse manner
# s1 = "Welcome to all"
# print(s1[::-1])

# ! ---> Eg:1
# wap to find the number of lower case letters
# s1 = "HEY there you aRE"
# count = 0
# for i in s1:
#     if i.islower():
#         count+=1
# print("The total num of lower case letters: ", count)

# ! -----> Eg:2 r --> "$"
# s1 = 'restarter'
# s1 "IMAGIN"
# fst = $1 [0]
# bal = s1 [1:]
# txt = bal.replace(fst, "$")
# print(fst+txt)

s1 = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum".
s1= s1.strip()

chracters = len(s1)
print(chracters)

words = s1.split(" ")
print(len(words))

sentenses = s1.split('.')
for val in sentenses:
    if val =='';
        index = sentenses.index('')
        sentenses.pop(index)
print(len(sentenses))

space = 0
for val in s1:
    if val ==" ":
space=space+1
print(space)














































