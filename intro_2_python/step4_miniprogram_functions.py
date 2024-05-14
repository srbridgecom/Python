#The following uses default values for variables
def welcome(name='learner', location='this area'):
    print("Hi", name, "welcome to", location)

welcome()

print("\n----------\n")

#The following uses default values for variables
# we are going to repeat the above code but grab names
def welcome(name='learner', location='this area'):
    print("Hi", name, "welcome to", location)

welcome()

welcome(name='john2')

welcome(location='this is area2')

welcome(name='john3', location='this is area3')
