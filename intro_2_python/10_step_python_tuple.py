#srbridge.com
#https://github.com/srbridgecom
#https://www.facebook.com/srbridge
#https://www.linkedin.com/in/r-bridge-3baa332a4/
#Python

#create a tuple
my_numbers = (1, 2, 3)
the_same = 1, 2, 3
my_strings = ('Hello', 'World')
my_mixed_tuple = ('Hello', 123, True)


#create tuple using constructor
tuple([0,1,2])
(0, 1, 2,)
    
    
#tuple holding 1 item
#Python sees the number one, surrounded by useless 
#parentheses on the first try, so Python strips down 
#the expression to the number 1. However, we added a 
#comma in the second try, explicitly signaling to Python 
#that we are creating a tuple with just one element.
t = (1)
1
t = (1, )
(1, )


#using tuple, combine multiple lists
#* operator unpacks the list
l1 = [1, 2, 3]
l2 = [4, 5, 6]
t = (*l1, *l2)
t
(1, 2, 3, 4, 5, 6)


#multiple assignments using python tuple
person = ('Erik', 38, True)
name, age, registered = person
name
'Erik'


#unpacking tuples works great in conjunction with
#a function that returns multiple values. It’s a 
# neat way of returning more than one value without
#having to resort to data classes or dictionaries:
def get_user_by_id(userid):
    return name, age

name, age = get_user_by_id(4)


#access tuple using index numbers like [0]
my_mixed_tuple = 'Hello', 123, True
my_mixed_tuple[0]
'Hello'
my_mixed_tuple[2]
#True


#you cannot append, create a new tuple to pull data
#What we did was unpack t1, create a new tuple with the 
#unpacked values and two different strings and assign 
#the result to t again.
t1 = (1, 2, 3)
t = (*t1, 'Extra', 'Items')
t
(1, 2, 3, 'Extra', 'Items')


#how long is the tuple, use len
t = 1, 2, 3
len(t)
#3


#convert tuple to a list
t = 1, 2, 3
list(t)
[1, 2, 3]

#convert tuple to string
t = (1, 2, 3)
print(t)
(1,2,3)
str(t)
'(1,2,3)'

