#srbridge.com
#https://github.com/srbridgecom
#https://www.facebook.com/srbridge
#https://www.linkedin.com/in/r-bridge-3baa332a4/
#Python

#PROGRAM to accept input
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
