# 1.) Python program to capitalize the first and last character of each 
# word in a string
# 2.) Input : 128
# Output : Yes
# 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
# 3.)l1=[1,2,3,4], l2=[5,6,7,8]
# Add both l1 and l2, ans=[6, 8, 10, 12]

'''*(1)
s1 = input("enter string: ")
fst = s1[0].upper()
lst = s1[-1].upper()
print(fst+s1[1:len(s1)-1]+lst)
'''

'''*(2)
n = 128
temp = n
f1 = 0
while n!=0:
    rem = n%10
    check= temp % rem
    if check!=0:
        f1=1
    n = n//10

if f1==0:
    print("yes")
else:
    print("no")
'''


l1 = [8,9,0,7]
l2 = [7,6,5,4]
l3=[]
for val in range(len(l1)):
    ans =l1[val]+l2[val]
    l3.append(ans)
print(l3)






























    
