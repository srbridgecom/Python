#srbridge.com
#https://github.com/srbridgecom
#https://www.facebook.com/srbridge
#https://www.linkedin.com/in/r-bridge-3baa332a4/
#Python

#dictionary also known as associative array

#create a dictionary
phone_numbers = {'jack': ' 070-123', 
                 'pete': '010-248'}
my_empty_dictionary = { }

phone_numbers['jack']
#OUTPUT is 070-123

phone_numbers['pete']
#OUTPUT is 010-248

#add or remove from the dictionary 
phone_numbers['eric'] = '06-1010'
del(phone_numbers['jack'])
phone_numbers
#OUTPUT is {'pete': '010-248', 'eric': '06-1010'}


#Another way to retrieve a single value from a dictionary is using the get-method. 
# The advantage? It returns a default value, None, if the key was not found. 
# You can specify your own default value too. With the get-method, you don’t 
# have to surround the operation with a try… except. It’s ideal when working 
# with configuration data that is parsed from YAML or JSON files, where your
# software offers defaults for unset configuration items.
config = { 'host': 'example.org'}
config.get('port', 80)
#OUTPUT =    80
config.get('schema')
#OUTPUT =        ------- blank/nothing/no output

#overright a dictionary entry and assign a new entry
phone_numbers = { 'jack': '070-0123',
                 'pete': '010-2488'}
phone_numbers['jack'] = '4321'
#jack is now replace with 4321

#TRY/EXCEPT  If a requested key does not exist, an exception of type KeyError is thrown:
phone_numbers['lisa']
#OUTPUT IS 
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#KeyError: 'lisa'

#anything can be in a dictionary, 
#you can put dictionaries and Python lists inside your dictionary and access the 
# nested values in a very natural way:
a = { 'sub_dict': { 'b': True }, 
      'mylist': [100, 200, 300] }
a['sub_dict']['b']
#OUTPUT = TRUE
a['mylist'][0]
#output = 100


#VALID KEYS
#You can go pretty wild on your dictionary keys, too. The only requirement is that the 
# key is hashable. Mutable types like lists, dictionaries, and sets won’t work and result 
# in an error like: TypeError: unhashable type: ‘dict’.
# Besides this limitation, you can use all data types as a dictionary key, including native 
# types like a tuple, float and int or even a class name or object based on a class.
my_dictionary = { int:1, float:2, dict: 3 }
my_dictionary[dict]
#OUTPUT = 3

class P:
    pass

my_dictionary[P]=1
p = P()
my_dictionary[p]=2

#A more likely use case is the use of numbers as keys. 
runners = { 1000: 'Jack', 1001: 'Eric', 
                1002: 'Lisa' }
runners[1001]
#OUTPUT = 'Eric'


#Using the dict() constructor
dict([ ('Jack', '070-02222748'), 
           ('Pete', '010-2488634'), 
           ('Eric', '06-10101010') ])
{'Jack': '070-02222748', 'Pete': '010-2488634', 'Eric': '06-10101010'}


#you can also use dictionary comprehensions to create a new dictionary.
# While a list only contains values, a dictionary contains key/value pairs.
{x: x**2 for x in (2, 4, 6)}
#OUTPUT = {2: 4, 4: 16, 6: 36}

#Using dict.fromkeys
#The dict.fromkeys(keys, value) method creates a new dictionary, based on the 
# list of keys supplied to it. The value of all elements will be set to the 
# supplied value, or None by default, if you don’t supply a value.
names = ['Eric', 'Martha', 'Ellen']
phone_numbers = dict.fromkeys(names, None)
phone_numbers
#OUTPUT = {'Ellen': None, 'Eric': None, 'Martha': None}


#Parse Json to dictionary
import json

jsonstring = { "name": "erik"; "age": 38,
                "married": true}'
json.loads(jsonstring)
#OUTPUT = {'name': 'erik', 'age': 38, 'married': True}   
                
                
#Check if a key exists in a Python dictionary
'Jack' in phone_numbers
#OUTPUT = True

'Jack' not in phone_numbers
#OUTPUT = False


#Getting the length of a Python dictionary
#The built-in Python len() function returns the number of key/value pairs in a dictionary:
phone_numbers = { 'Jack': '070-02222748', 
                      'Pete': '010-2488634', 
                      'Eric': '06-10101010' }
len(phone_numbers)


#Dictionary view objects
#Some built-in dictionary methods return a view object, offering a window on your 
# dictionary’s keys and values. Before we start using such view objects, there’s an 
# important concept you need to understand: values in a view object change as the
# content of the dictionary changes. 
phone_numbers = { 'Jack': '070-02222748', 
                  'Pete': '010-2488634',
                  'Eric': '06-10101010' }
names = phone_numbers.keys()
numbers = phone_numbers.values()
phone_numbers['Linda'] = '030-987612312'
print(names)
print(numbers)

# Loop through a view object with:
for number in numbers:
    print(number)
#OUTPUT = The output of this code is dict_keys(['Jack', 'Pete', 'Eric', 'Linda']). 
# As you can see, Linda is part of the list too, even though she got added after creating the names view object.
    
    
#another version non interactive
phone_numbers = { 'Jack': '070-02222748', 
                  'Pete': '010-2488634',
                  'Eric': '06-10101010' }
names = phone_numbers.keys()
numbers = phone_numbers.values()
phone_numbers['Linda'] = '030-987612312'
print(names)
print(numbers)
# Loop through a view object with:
for number in numbers:
    print(number)
#OUTPUT = The output of this code is dict_keys(['Jack', 'Pete', 'Eric', 'Linda']). 
# As you can see, Linda is part of the list too, even though she got added after creating the names view object.


#dict.items(): loop through a Python dictionary
#The items() method of a dictionary returns an iterable view 
#object, offering both the keys and values
phone_numbers.items()
dict_items([('Jack', '070-02222748'), 
            ('Pete', '010-2488634'), 
            ('Eric', '06-10101010')])
    for name, phonenr in phone_numbers.items():
    print(name, ":", phonenr)
    
#OUTPUT 
#Jack : 070-02222748
#Pete : 010-2488634
#Eric : 06-10101010


#get dictionary keys from list and sorted
phone_numbers = { 'Jack': '070-02222748', 
                      'Pete': '010-2488634', 
                      'Eric': '06-10101010' }
list(phone_numbers)
#OUTPUT === ['Jack', 'Pete', 'Eric']

sorted(phone_numbers)
#OUTPUT === ['Eric', 'Jack', 'Pete']

#MERGE a dictionary
merged = dict1 | dict2


#Comparing Python dictionaries
first_dict  = { 'a': 1, 'b': 2, 'c': 'a string' }
second_dict = { 'a': 1, 'b': 2, 'c': 'a string' }
first_dict == second_dict
#OUTPUT =  True


#Built-in Python dictionary methods
#Each dictionary inherits some handy built-in functions, as listed in the following table:

Method	                    What is does	                                                            Example
clear()	                    Remove all key/value pairs (empty the dictionary)	                        phone_numbers.clear()
get(key)	                Get a single item with the given key, with an optional default value	    phone_numbers.get('Martha', 'Unknown person')
items()	                    Returns a view object containing key-value pairs from the dictionary	    phone_numbers.items()
keys()	                    Returns a view object with a list of all keys from the dictionary	        hone_numbers.keys()
values()	                Returns a view_object with a list of all values from the dictionary	        phone_numbers.values()
pop(key, default_value)	    Returns and removes the element with the specified key	                    phone_numbers.pop('Martha')
popitem()	                Returns and removes the last inserted item (Python 3.7+) or a random item	phone_numbers.popitem()
setdefault(key, value)	    Returns the value of the specified key. If the key does not exist, it’s 
                            inserted with the given value	                                            phone_numbers.setdefault('John Doe', 1234)
update(iterable)	        Add all pairs from given iterable, e.g. a dictionary	                    Add all pairs from a given iterable, e.g. a dictionary
