#quick recap test\, create an infinite loop that keeps asking for names,
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
