#srbridge.com
#https://github.com/srbridgecom
#https://www.facebook.com/srbridge
#https://www.linkedin.com/in/r-bridge-3baa332a4/
#Python
#quick recap test, create an infinite loop that keeps asking for names,
#keeps greeting us using the entered name
def say_hi(name):
    if name == '':
        print("you didn't enter your name!")
    else:
        print('Hi ...')
        for letter in name:
            print(letter)

while True:  #this creates the loop, delete this and the prog ends after 1 name
    name = input('Hi, enter your name:')

    say_hi(name)


def display_name(name):
    if name == '':
        print("theres no name displayed!")
    else:
        print('WASSUP')
        for letter in name:
            print(letter)

while True:
    name = input('hey, whats your name')

    display_name(name)
