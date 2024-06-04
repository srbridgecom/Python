#srbridge.com
#https://github.com/srbridgecom
#https://www.facebook.com/srbridge
#https://www.linkedin.com/in/r-bridge-3baa332a4/
#Python

#Python set is a collection of distinct elements. The set has some things in 
# common with Python lists and tuples, but there are important differences:
# A Python set can only contain unique values
# Sets are unordered
# More formally: sets are unordered collections of distinct objects. 
#why use a set
#The most common one is to remove duplicates from a sequence (like lists, as demonstrated before)
#Many use them to perform membership testing (is an element present in this set of unique elements)
#Finding the difference between two sets
#Union: combining sets and only keeping unique elements
#Intersection: which elements are present in both sets
#Finding subsets and supersets


#how to create a set
names = {"eric", "ryan", "john"}


#create a python mixed set
mixed_set = { 'a', 1, (1, 2) }


#create an empty set
my_set = set()
my_set.add(1)
my_set.add('eric') #add elements to set with add command


#you can add elements to a set using the add method on a 
#set object. If you want to add multiple elements at once, you need to 
#use the update method and provide an iterable object like a list, range, or tuple:
my_set = set()
my_set.update(range(3))
my_set.update(['a', 'b'])
print(my_set)
#output is {0, 1, 2, 'b', 'a'}


#use set function to convert iterable object into a set
print( set([1, 2, 3]))
#output is {1, 2, 3}
print( set(range(3)))
#output is {0, 1, 2}


#use set comprehension to create a set
#filter a set comprehension, let’s filter punctuation and space characters as well:
#keep in mind, sets have no order, your output is mixed results
my_set = { x for x in 'hi my name is' if x not in '.,'}
print(my_set)
#output is {'n', 'a', 'e', 'i', 's', 'y', 'h', 'm'}


#dedpulicate lists Deduplication is the process of removing duplicates
# and converting a list to a set is by far to easiest way to do this
my_list = [1, 1, 1, 2, 3, 4, 4, 4, 4, 2, 2, 2]
my_set = set(my_list)
print(my_set)
#output is {1, 2, 3, 4}


#convert a set to list - create a new list with the set as the main argument
A = {1, 2, 3}
my_list = list(A)
print(my_list)
#output it now [1, 2, 3]


#Finding the difference between Python sets 
# Let’s define two sets, A and B, and find the difference between them. 
# What is the difference between two sets? When looking at the Venn diagram, 
# we want to find the elements that are only present in A. In other words, 
# we want to get rid of any overlapping elements that are also in B. Or, 
# even more specific: we want all elements that are in A but not in A ∩ B. 
#use Venn diagram
#EXPLANATION A and B have some overlap: the numbers 3, 4, and 5 are in both sets. 
# These numbers fall into the section that is labeled with A ∩ B when looking 
# at the Venn diagram. If we want only the unique numbers that are in A, 
# we ‘subtract’ B from A by using A – B. When we only want the unique set of 
# numbers from B, we subtract A from B: B – A.

#using minus
A = { 1, 2, 3, 4, 5 }
B = { 3, 4, 5, 6, 7 }
print(A-B)
#OUTPUT IS    {1, 2}

#reverseoperation 
print(B-A)
#OUTPUT is {6, 7}


# find symmetrix difference between python sets USING ^ 
#The symmetric difference between two sets consists of the elements that are 
#either in set A or in set B, but not in both. In other words: 
#all the elements in A plus the elements from B, minus the A ∩ B 
#part. To find the symmetric difference, we can use the ^ operator:
A = { 1, 2, 3, 4, 5 }
B = { 3, 4, 5, 6, 7 }
print(A^B)
#output is  {1, 2, 6, 7}


#Find the INTERSETION of sets with & operator
A = { 1, 2, 3, 4, 5 }
B = { 3, 4, 5, 6, 7 }
print(A&B)
#output is {3, 4, 5}


#SUBSET and SUPERSET
#If A is a subset of B, all elements of A are also present in B. However, subset
#A can be smaller than set B, meaning some elements in B might not be present in 
#A. So if A overlaps almost completely, but has one element that’s not present 
#in B, it’s not a subset of B. 
#Check is A is a subset of b with <
#check if B is a superset of A with >

A = { 1, 2, 3, }
B = { 1, 2, 3, 4, 5 }
C = { 1, 2, 3, 10 }

print( A < B ) #is a subset of b?
#output  = True

print( C < B) #is C superset of b?
#output = FALSE    (has a 10)

print( B > A) #is B superset of A?
#output = True

print( B > C ) # is b superset of c?
#output = False

print( A <= A)
#output = True


#add 2 python sets together in UNION
A = { 1, 2, 3 }
B = { 3, 4, 5 }
print (A|B)
#output is = {1, 2, 3, 4, 5}



#Name	                Operator    Method example	            What it does
#Union	                A | B	    A.union(B)	                Create a set that combines A and B
#Intersection	        A & B	    A.intersection(B)	        Create a set with elements common between A and B
#Difference	            A - B	    A.difference(B)	            Create a set with elements that are not in B
#Symmetric difference	A ^ B	    A.symmetric_difference(B)	Create a set with elements that are in A or B, but not in both
#Is superset?	        A >= B	    A.issuperset(B)	            Returns True if every element of B is in A
#Is subset?	            A <= B	    A.issubset(B)	            Returns True if every element of A is in B
#Is disjoint?	        No operator	A.isdisjoint(B)	            Returns True if A has no elements in common with B
#Is proper superset?	A > B	    There’s no method	        True if A >= B and A != B
#Is proper subset?	    A < B	    There’s no method	        True if A =< B and A != B
#add	                            A.add(elem)	                Add element to set
#remove	                            A.remove(elem)	            Remove element from set
#discard	                        A.discard(elem)	            Remove element from the set if it is present (save you a presence check)
#pop	                            A.pop()	                    Remove and return an arbitrary element from the set (raises KeyError if the set is empty)
#clear	                            A.clear()	                Remove all elements from the set
