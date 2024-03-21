# 2.) Find the uncommon words from 2 strings
# s1 = "Hello how are you"
# s2 = "Hello how is"
'''
s1 = "Hello how are you"
s2 =  "Hello how is"

s1 = s1.split(" ")
s2 = s2.split(" ")
for val in s1:
    if val not in s2:
        print(val)
for val in s2:
    if val not in s1:
        print(val)
'''
# 3.) Wrire a code print the 8th fibanochi number
# 0,1,1,2,3,5,8
'''
num = 8
n1 = 0
n2 = 1

for val in range(num):
    ans = n1+n2
    print(ans)
    n1 = n2
    n2 = ans
print(ans)
'''
# ! Constructors
# ? Eg:2
# * unparametarised constructor
'''
# class profile:
#    def _init__(self):
#        print("hello world")
        
# obj = profile()
# obj.__init__()
'''
# ? Eg: 3
# * Parametarised Constructor
'''
class profile:
    def __init__(self, id, name, age):
        print(id, name, age)
        
obj = profile(1, "sid", 29)
'''

# ? Eg:4
'''
class c1:
    email = "sid@gmail.com"
  
    def m1(self):
        name = "sid"
        place= "cbe"
        print(name, place)
        print(self.email)
        
object = c1()
object.m1()
'''

# ? Eg:5
'''
class c1:
    def m1(self):
        name = "sid"
        age = 28
        return name, age
    def display(self):
        # ! print(name, age)
        # ! print(self.name, self.age)
        print(self.m1())

object = c1()
object.display()
'''

# ? Eg:6
# ? To use the variable inside the constructor in another methods
'''
class class1:
    def __init__(self):
       self.name = "sid"
       self.email = "sid@gmail.com"
       # return name, email #error --> cannot use return with constructor
    
    def display(self):
        print(self.name, self.email)
        
c1 = class1()
c1.display()
'''

# ! -----> Inheritance
# The process of utilising ythje methods and attributes of parent class
# throught the object of child class it is called as inheritance

# 5 types of Inheritance
# Single Inheritance
# Multilevel Inheritance
# Multiple Inheritance
# Hybrid Inheitance
# Heirarichal Inheritance

# * Single Inheritance
# ? It has only one parent class and only one child class
# ! Eg:1
'''
class parent:
    def m1(self):
        print("Iam parent class")
    
class child(parent):
    def m2(self):
        print("Iam child class")

obj = child()
obj.m1()
'''
# ! Eg:2
'''
class cl:
    def __init__(self):
        print("Iam constructor from parent class")
   
class childl(cl):
    pass

obj = childl()
'''
# ! Eg:3
'''
class parent:
    name = "sidhu"
    
class child(parent):
    name = "name1"
    
    def display(self):
        print(self.name)
        
d = child()
d.display()
'''

# ! Multilevel Inheritance
# ? Eg:1
'''
class voice:
    def sound(self):
        print("All the animals have their own voices")
          
class dog(voice):
    def dog_voice(self):
        print("bark")
        
class cat(dog):
    def cat_voice(self):
        print("Meow")
        
class parrot(cat):
    def parrot_voice(self):
        print("speak")


all = parrot()
all.dog_voice()
all.cat_voice
all.sound()
all.parrot_voice()
'''
# Eg:2
'''
class honda_city:
    def honda_city_engine_specs (self, cc, Hp, torque, fuel_type, num_of_piston):
        print(cc, Hp, torque, fuel_type, num_of_piston)
        
    def honda_city_body_specs (self, color, weight, height, length, vehicle_type):
        print(color, weight, height, length, vehicle_type)
        
class amaze (honda_city):
    def amaze_engine_s (parameter, torque, Any_fuel_type, num_of_piston):
        print(cc, Hp, torque, fuel type, num_of_piston)
        
    def amaze_body_specs (self, color, weight, height, length, vehicle_type):
        print(color, weight, height, length, vehicle_type)
        
class civic(amaze):
    def civic_engine_specs (self, cc, Hp, torque, fuel_type, num_of_piston):
        print(cc, Hp, torque, fuel_type, num_of_piston)
        
    def civic_body_specs (self, color, weight, height, length, vehicle_type):
        print(color, weight, height, length, vehicle_type)
        
class Honda(civic):
    pass

honda Honda()
honda.honda_city_engine_specs (1500, 230, 2979, "petrol", 4)
honda.civic_body_specs ("white", 2000, 5.5, 8, "Hatchback")
'''
# Eg:3
'''
class while_pertol:
    def function_w(self):
        print("used to Airplans")
        
class Organic_petrol:
    def function_o(self):
        print("used for Bike, cars")
        
class premium_petrol:
    def function_p(self):
        print("spots cars, bikes")
        
class petrol (while_pertol, Organic_petrol, premium_petrol):
    def defanition(self):
        print("Petrols types")

p= petrol()
p.defanition()
p.function_o()
'''
# Eg:4
# MRO --> Method resolution Order
'''
class addition:
    def add(self, a, b):
        print(a+b)
        
    def mul(self, a, b):
        print(a%b)
        
class subract:
    def sub(self, a, b):
        print(a-b)
class multiply:
    def mul(self, a, b):
        print(a*b)
class division(addition, subract, multiply):
    def div(self, a, b):
        print(a/b)
        
calc = division() 
# calc.add(3, 4)
calc.mul(4, 2)
'''
# Heirarichal Inheritance
'''
class category:
    def weight(self, weight):
       print(weight)

    def display(self, color, taste):
        print(color, taste)
        
class Tomato(category):
    def tomato_specs(self):
        color="black"
        taste = "neutral taste"
        self.display(color, taste)
        
class carrot(category):
    def carrot_specs(self):
        color="green"
        taste = "sweet"

c = carrot()
c.carrot_specs()
c.weight("30gms")
t = Tomato()
t.tomato_specs()
t.weight("20gms")
'''
# ! Hybrid inheritance
# ? The combination of above 4 inheritance is called Hybrid inheritance

class c1:
    def ml(self):
        print("Class1")
        
class c2:
    def m2(self):
        print("class2")
        
class c3:
    def m3(self):
        print("Class 3")
        
class c4(c3):
    def m4(self):
        print("Class 4")
        
    def m3(self):
        print("iam m3 from c4")
        
class c5(c4):
    def m5(self):
        print("Class 4")
        
class c6(c5, c3):
    def m6(self):
        print("Class 4")
        
obj = c6()
obj.m3()






















 





































































































