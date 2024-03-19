# ! Eg:2
# Function with parameter
# def greeting(name):# name is parameter
#     print("Welcome", name)

# for val in range(3):
#     username input("Enter the name: ")
#      greeting(username) # username is argument

#  ! Eg:3
# def profile(name, age, place):
#   txt = "My name is {}. Iam {} years old. Iam from {}."
#    print(txt.format(name, age, place)) 
# profile("amju", 22, "kadapa")

# ! Eg:4
# ? Function with return statement

# return
# 1.) A variable declared inside the function csn be accessed outside the function

# def f1():
# z = 8
# f1()
# print(z) # error --> cannot use outside the function
# using return
# 2.) return does not prrint anything
# 3.) we cannot write any code below return statement


# def f1(a, b):
#    c = a*b
#    return c
# print(f1(6,8))
# obj = f1(6,8)
# obj1 = f1(4,6)

# def gracemark(object):
#     print(object+4)
# gracemark(obj)
# gracemark(obj1)

'''
# ? Problem(1):
def palindrome(n):
    string = str(n)
    rev = str(n) [::-1]
    if string==rev:
        print(n, "Palindrome")
    else:
        print("Not palindrome")
a = int(input("Enter the value: "))
palindrome(a)
'''

# ? Based on the declaration of parameter and args
# ? functions are divided into 5 catagories

# Positional args
# keyword args
# default args
# variable length args
# keyword variable length args

'''
# * Positional args
# The psition of parameter have to be same as position of arguments
# ! Eg:1
def profile(name, phone, mark):
    txt = "My name is {}. My phone number is {}. I got {} marks."
    print(txt.format(name, phone, mark))
    
profile (9878776767, "sidhu", 97) # unexpected output
'''

'''
# *Keyword args
# ! Eg:1
# ? To overcome the disadvantage of position args, we use keyword arg
# ? It is the process of initialising the paremeter with the args while calling the
# ? function
def profile(name, phone, mark):
    txt = "My name is {}. My phone number is {}. I got {} marks."
    print(txt.format(name, phone, mark))
    
profile(name="sid", mark=96, phone=1234567890)
'''

'''
#todo ---> Exception of keyword args function
def profile(name, phone, mark):
    txt = "My name is {}. My phone number is {}. I got {} marks."
    print(txt.format(name, phone, mark))
    
# profile(name="sid", 123445567, mark=98) #error --> positional arg follow keywordargs   
# profile(123445567, name="sid", mark=98) #error --> name has multiple values
profile("sid", mark=98, phone=12345678)
'''

'''
# * Default args
# The method of assigning the argumengt to the parameter while declaring the
# fuunction
#! Eg:1
def profile(name, phone, place="kadapa"):
    txt = "My name is {}. My phone number is {}. I am from {}."
    print(txt.format(name, phone, place))
    
profile("sid", 8767676767)
'''

'''
# ! Eg:2
def profile(name, phone, place="kadapa"):
    txt = "My name is {}. My phone number is {}. I am from {}."
    print(txt.format(name, phone, place))
    
profile("sid", 8767676767,"Guntur")
'''

'''
#! Eg:3
def profile(name, phone, place="KADAPA"):
 if place == "Kadapa" or place=="KADAPA" or place=="kadapa":
     txt = "My name is {}. My phone number is {}. I am from {}."
     print(txt.format(name, phone, place))
 else:
     print("You are not eligible to Sigrlup")
profile("sid", 8767676767)
'''
'''
# ! Exception
def profile(name, place="KADAPA", phone): # error --> coz default args
                                          # positional param
    if place == "Kadapa" or place=="KADAPA" or place=="kadapa":
        txt = "My name is {}. My phone number is {}. I am from {}."
        print(txt.format(name, phone, place))
    else:
 print("You are not eligible to Signup")
pr0file("sid", 8767676767)
'''

'''
#  * Variable length params
# ! Eg:1
# To pass more then 1 arg to a paremeter means we use variable leng
# To convert normal paremeter to variable length param, add to th

# name = "sid", 'name2', 'name3'
def profile(*name):
    for val in name:
        print("My name is", val)
profile("sid", 'name2', 'name3')
'''
'''
# ! Eg:2
def profile(*name, age):
    for val in name:
        print("My name is", val, "may age is", age)
profile("sid", 'name2', 'name3', 28) #errror --> age has no args
'''
'''
# Eg:2
def profile(age, *name):
    for val in name:
        print("My name is", val, "may age is", age)
profile(28, "sid", 'name2', 'name3')
'''
'''
# * Keyword variable length args
# ! Eg:1
def price(**price_list):
    print(price_list)
    
price(shirt=1000, iphone=80000)

d1 ("a":100, "b": 200, "c":300)
d1= dict(a=100, h=200, c=300)
print(d1)
'''
'''
#n=5
#(1:1, 2:4, 3:9, 4:16, 5:25)
n = int(input("Enter the number: "))
d1 = {}
for val in range(1, n+1):
    d1[val] = val**2
print(d1)
'''
'''
def dict1(n):
    d1 = {}
    for val in range(1, n+1):
        d1[val] = val**2
    print(d1)
dict1(5)
'''


# ! -------> object oriented programming
# The paradigms of objects oriented progarmming are

# class
# ojects
# inheritance
# polymorphism
# abstraction
# encapsulation

'''
# ! class is a blue print of an object
# l1 [1,2,3,4,5,6]

#? Eg:1

# class c1:
#   namel = "sidhu"
#   print(namel)
'''
'''
# ? Eg:2
# class person:
     name = "sidhu"

# c = person() # c os object
# The process of creation of an object is called as Instantiation
# print(c.name)
'''
'''
# ? Eg:3
# create of a method
# When the function is created with a class is called as method

class person:
    def display(person):
        print("Hello welcome to classes")

p = person()
p.display()
'''
'''
# ? Eg:5

class person1:
    fname = "sidhu" #attribute or static variable
    Iname = "T"

    def first_name(self):
        print(self.fname)
    def full_name(self):
        print(self.fname+" "+self.Iname)
    
p = person1()
p.first_name()
p.full_name()
'''

# ? Eg:6
# constructors -->_init_()
# This is a special mrthod which has the ability to execute itself without
# calling it manually through the process of instantiation

class profile:
    def __init__(self): # Constructor method
        print("hey")
    
p = profile() # throught this process
























 


