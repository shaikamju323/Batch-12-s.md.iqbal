#--->while loop
#---->break using while loop

#eg:1
#1) Iterate from 20 to 30 and break the loop in 27
'''
a = 20
while a<20:
     print(a)
     a+=1
'''
#eg:2
'''
a =20
while a<31:
    print(a)
    if a ==27:
        break
    a+=1
'''
#eg:3
'''
a = 20
while a<31:
    if a ==27:
        print(a)
        break
    a+=1
'''

# ! -----> continue
# ---> Eg:4
'''
a =20
while a<31:
    if a==27:
        continue
    print(a)
    a=a+1
'''
'''
a =20
while a<31:
    a=a+1
    if a==27:
        continue
    print(a)
'''
'''
# Eg:5
i = 12
while i<22:
    i=i+1
    if i==11:
        break
    print(i)
'''
'''
i = 12
sum=0
while i<23:
    sum=sum+i
    i+=1
print(sum)
'''
#i = 20
#sum=0
#count =0
#while i<=30:
#    sum=sum+i
#    count+=1
#    i+=1
#print(sum/count)
'''
#! -------> Nested for loop
#Eg:1
for row in range(1,3+1):
    for col in range(1,4+1):
       print(row,col)
'''
#Eg:2
#* * * *
#* * * *
#* * * *
#* * * *
'''
rows = int(input("enter the rows: "))
cols = int(input("enter the cols: "))
           
for row in range(rows):
    for col in range(cols):
        print("*" , end=" ")
    print()
'''
'''
sum = 0
for row in range(5):
    for col in range(5):
        sum=sum+1
        print(sum,end=" ")
    print()
'''
# ! to print stars in right angled triangle
'''
for row in range(0,6):
    for col in range(0,row+1):
        print("*",end=" ")
    print()
'''
##* * * * * *
##* * * * *
##* * * *
##* * *
##* *
##*
'''
for row in range(0,6):
    for col in range(row,6):
        print("*",end=" ")
    print()
'''
##* * * * *
##*       *
##*       *
##*       *
##* * * * *
'''
for row in range(5):
    for col in range(5):
        if col==0 or col==5-1 or row==0 or row==5-1: 
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
'''
##     *
##  *  *  *
## * * * * *
'''
for row in range(0,5):
    for col in range(0,6):
        if ((row==0 and col==3) or (row==1 and(col>=2 and col<=4)) or
                                 (row==2 and (col>=1 and col<=5))): 
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
'''

# ! ---> Datatypes
# Primary

# Number --> int, float complex
# String
# Boolean
# None

# Collection
# List
# tuple
# set
# dictionary

#?--> List
# 1.) if the collection of elements are sorounded by square brackets, it is considered # to be list
# ! eg:
# 11 [4, 7, 9, 9.89, "hello", 7+9j, [8, 9, 0]]

# * charactristics of list
# 1.) list have to be sorrrounded by []
# 2.) It is mutable (the elements in the list are changable)
# 3.) Every element inside list is indexed
# 4.) The elements inside list will be ordered format
# 5.) It can hold duplicate values
# 6.) Its heterogenous

# To access the elements in list
1st1 = [1, 4, 1, 7,89.7, 7.5, "p", "i"]
# print(lst1)

# --> Indexing
# In the collection datatypes like list, tuple, string, the elements will be alloted
# with predefined unique value called index value

# We have 2 types of indexing
# Positive indexing --> starts with @ from left hand side
# Negative indexing --> starts with -1 from right hand side

# ? ---> Positive indexing
# lst1 = [1,4,1,89,7.5,"p","i"]
# print(1st1[0])
# print(1st1[4])
# print(1st11[20]) --> error

# ?  -----> Negative indexing
# 1stl = [1, 4, 1, 7,89.7, 7.5, "p", "1"]
# print(1st1[-1]) 
# print(1st1[-5])

#?---> slicing
1st1 = [1, 4, 1, 7,89.7, 7.5, "p", "i"]
# 1st1[start_index:end_index: step]

# print(1st1[0:4])
print()







































































    




    
































































































































































    
    
