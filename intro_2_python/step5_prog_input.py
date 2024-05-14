#Using input to grab data, if data display
#prog will pause and ask for input, then print out line by line
#if you enter no name, get yelled at and exit
def say_hi(name):
    if name == '':
        print("There's no name, enter your name!")
    else:
        print("Hi .....")
        for letter in name:
            print(letter)

name = input("Enter your name:") #ask for input and assign it to variable name
say_hi(name)
