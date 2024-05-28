#srbridge.com
#https://github.com/srbridgecom
#https://www.facebook.com/srbridge
#https://www.linkedin.com/in/r-bridge-3baa332a4/
#Python

#create a list
my_list = [1, 2, 3]
empty_list = []
 
 
#also lists = 
my_list = [1, "Erik", { 'age': 39}]


#also, this is a list with 3 lists inside
game_board = [[], [], []]


#use list function
list(range(1, 4))
[1, 2, 3]
list ({1, 2, 2, 2, 3})
[1, 2, 3]
list( (1, 2, 3) )
[1, 2, 3]


#how to access the python lists element
#remember python starts counting at 0 - so to output position
#the answer 2, you call position 1
my_list = [1, 2, 3]
my_list[1]
# output is 2
my_list[0]
#output is 1
my_list[4]
Traceback (most recent call last):
    #File "<stdin>", line 1, in <module>
    #IndexError: list index out of range
    
    
#get the last element of a list
my_list = [1, 2, 3]
my_list[-1] #this calls the last element
# output is 3
my_list[-2] #this calls the 2nd to last element
# output is 2


#accessing nested list elements
my_list = [[1, 2], [3, 4], [5, 6]]
my_list[0]
#output will be [1, 2]


#append/adding to alist
my_list = [1, 2]
my_list.append('a')
my_list 
#output is [1, 2, 'a']
my_list.append(4)
my_list
#output is [1, 2, 'a', 4]


#merging lists
#add 2 lists together to make a 3rd
l1 = [1, 2]
l2 = [3, 4]
l3 = l1 + l2
l3
#output is now [1, 2, 3, 4]
#NOW to extend one list with another use the EXTEND METHOD
#l2 will stay as an individual list but still added on to l1
l1 = [1, 2]
l2 = [3, 4]
l1.extend(l2)
l1
#output is now [1, 2, 3, 4]


#POP items --- REMOVES AND RETURNS the last item unless you specify
my_list = [1, 2, 3, 4, 5]
my_list.pop()
#output is 5
my_list.pop()
#output is now 4
my_list.pop(0)
#output is now 1
my_list
#output is now [2, 3] ------4 - 5- 1 REMOVED


#using DEL to DELETE items
my_list = [1, 2, 3, 4, 5]
del(my_list[0])
my_list
#output is now  [2, 3, 4, 5]
del(my_list)
my_list
#output is now python traceback call...


#using REMOVE to remove a specific value
my_list = [1, 2, 3, 2, 5,]
my_list.remove(2)
my_list
#output is not [1, 3, 2, 5]


#how to remove or clear all items in the list
my_list = [1, 2, 3]
my_list.clear()
my_list
#OUTPUT is now .......... nothing []


#remove Duplicates from a list
# TRICK 1 convert to a set..... clean up then reconvert to list
my_list = [1, 2, 2, 3, 5]
my_set = set(my_list)
my_set 
#OUTPUT is now the conversion {1, 2, 3, 5}
list(my_set)
#output is now list again [1, 2, 3, 5]
#ANOTHER TRICK --- AKA TRICK 2
my_list = [1, 2, 2, 3, 5]
list(set(my_list))
#output is now list again [1, 2, 3, 5]


#replacing items in the list
my_list = [1, 2, 3, 4, 5]
my_list[0] = 400
my_list
#output is now [400, 2, 3, 4, 5]


#get list length 
my_list = [1, 2, 3]
len(my_list)
#output is 3


#check is an item is inside a list
my_list = [1, 2]
if 2 in my_list:
    print("2s inthe list")
#output 2s inthe list


#find the index or position of an itme in the list
my_list = [1, 2, 3, 4]
my_list.index(4)
#output is 3


#sorting a python lists
#We can not sort all lists, since Python can not compare all types with each 
#other. For example, we can sort a list of numbers, like integers and floats, 
#because they have a defined order. We can sort a list of strings as well since 
#Python is able to compare strings too.
#However, lists can contain any type of object, and we can’t compare completely 
#different objects, like numbers and strings, to each other. In such 
#cases, Python throws a TypeError:

#sort in ascending order
my_list = [4, 2, 1, 3]
my_list.sort()
my_list
#output is [1, 2, 3, 4]

#SORT in descending order
my_list = [ 4, 2, 1, 3]
my_list.sort(reverse=true)
my_list
#output is [4, 3, 2, 1]

#sort using the SORTED() command
my_list = [10, 2, 5, 4]
sorted(my_list)
#output is now [2, 4, 5, 10}
my_list
#output is [10, 2, 5, 4]

#sorted in descending order
my_list = [10, 2, 5, 4]
my_list.sorted(my_list, reverse=True)
#output [10, 5, 4, 2]


#SLICING or obtaining a part of a list
#slice exmaple is    my_list[start:stop:step]
#    start is the first element position to include
#    stop is exclusive, meaning that the element at position stop won’t be included.
#    step is the step size. more on this later.
#    start, stop, and step are all optional.
#    Negative values can be used too.

my_list = [1, 2, 3, 4, 5, 6]
my_list[0:3]  #get the 1st 3 elements
#output is now [1, 2, 3]

my_list[:3]  #start is 0 by default
#output is now [1, 2, 3]

my_list[4:]  # skip the first 4 elements
#output, is now [5, 6]

#STEP VALUE
my_list = [1, 2, 3, 4, 5, 6]
my_list[::2] #skip one
#output is now [1, 3, 5]


#REVERSE a python list
#    An in-place reverse, using the built-in reverse method that every list has natively
#    Using list slicing with a negative step size results in a new list
#    Create a reverse iterator, with the reversed() function
my_list = [1, 2, 3, 4]

my_list.reverse()   #in place reverse
print('using list reverse', my_list)
my_list.reverse()   #revert the list

my_list2 = my_list[::-1] #created a list that reverted
print('reverse the 2nd', my_list2)    
    
rev = reversed(my_list)   #use a reversed iterator
print('Reversed iterator', list(rev))  


#reverse with built in reverse method
my_list = [1, 2, 3, 4]
my_list.reverse()
my_list
#output is [4, 3, 2, 1]
my_list.reverse()
my_list
#output is now [1, 2, 3, 4]

#reverse with slicing - created a new list
#Although you can reverse a list with the list.reverse() method 
#that every list has, you can do it with list slicing too, using a 
# negative step size of -1. The difference here is that list
# slicing results in a new, second list. It keeps the original list intact:
my_list = [1, 2, 3, 4]
my_list[::-1]
#output is now [4, 3, 2, 1]
my_list
#output is now [1, 2, 3, 4]

#you can use the reversed() built-in function, which creates an iterator that returns 
# all elements of the given iterable (our list) in reverse. This method is quite 
# cheap in terms of CPU and memory usage. All it needs to do is walk backward 
# over the iterable object. It’s doesn’t need to move around data and it doesn’t 
# need to reserve extra memory for a second list. So if you need to iterate over 
# a (large) list in reverse, this should be your choice.
# Here’s how you can use this function. Keep in mind, that you can only use the 
# iterator once, but that it’s cheap to make a new one:
my_list = [1, 2, 3, 4]
rev = reversed(my_list)
rev
# output <list_reverseiterator object at 0x0000023DB96A25C0>
for i in rev:
    print(i)
#output is now
#4
#3
#2
#1
