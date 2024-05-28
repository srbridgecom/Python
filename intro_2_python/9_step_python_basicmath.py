#srbridge.com
#https://github.com/srbridgecom
#https://www.facebook.com/srbridge
#https://www.linkedin.com/in/r-bridge-3baa332a4/
#Python

import random


# assign variable int1 with a number using int command
int1 = int('100')
int2 = int('200')
int3 = int('300')

#assign variable str1 the STRING number 100 as a string
str1 = str(100)
str2 = str(200)
str3 = str(3300)

#print it out
print(int1, int2, int3, str1, str2, str3)

#generate random number between 1 & 10
random.randint(1,10)
print(random)

#use TYPE() to check if a value is an integer; is 2 an integer?
type(2)
int
if isinstance(2, int):
    print('an integer')

#floating point numbers
f = 1.45

#variable f becomes 2.0
f = float(2.0)
f = float(2)
f = float("2")

#use scientific notation
f = 1.45e3 #f now becomes 1450.0

#use math with float
x = 1.45
y = 4.51
x = x + y

#how to round a number
f = 1.4567
round(f)    #1
round(f, 2) #1.46

#round down with floor, round up with ceil
from math import, ceil
x = floor(1.23)    #x is now = 1
y = ceil(1.23)     #y is now = 2

#compare float
x = 1.23
y = 4.56

if x == y:
    print("x & y are equal")
else:
    print("x and y are not equal")
    
    
#convert float to int or string
my_int = int(1.22)    #variable my_int will be 1
my_str = str(2.23)    #variable my_str will be 2.23
