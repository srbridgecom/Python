#srbridge.com
#https://github.com/srbridgecom
#https://www.facebook.com/srbridge
#https://www.linkedin.com/in/r-bridge-3baa332a4/
#Python

#The provided code stub reads two integers from STDIN, a and b. Add code to print three lines where:
#    The first line contains the sum of two numbers.
#    The second line contains the difference of the two numbers (first – second).
#    The third line contains the product of two numbers. 
#
#Example     a = 3     b = 5     Print the following:    8   -2   15
#the following is provided by hackerrank
# if __name__ == '__main__':
#    a = int(input())
#    b = int(input())

#WHAT IS THIS CRAP? why even give us any starting code, it's confusing.
#I can tell you a = int(input()) means Cariable A is a integer and get the input from the keybord
#but it doesn't even display a message or instruction on input... like really? you will never see that in the real world, ever.

#let's Being
#start code/function
if __name__ == '__main__':
    a = int(input("Enter 1st number = "))      #modify it to explain to user, PLEASE Enter your 1st number and assign it to A
    b = int(input("Enter 2nd Number = "))      #modify it to explain to user, PLEASE Enter your 2nd number and assign it to B
    
    print("\n----------\n")     #spacing for clean code
     
    print ("The value of A is = ", a, "\n" "The value of B is = ", b, "\n")   #display a user friendly message stating it has worked!
    
    #NOW to satisfy the hackerrank 1st request
    print("hackerrank 1st request - The first line contains the sum of two numbers.", "\n", "A + B = ", a + b, "\n")
    #Now to satisfy the hackerrank 2nd request
    print("The second line contains the difference of the two numbers (first - second).", "\n", "A - B = ", a - b, "\n")
    #now, to satisfy the hackerrank 3rd request
    print("The third line contains the product of two numbers.", "\n", "A * B = ", a * b, "\n\n")
    print("\n----------\n")     #spacing for clean code

    
    #SOLVED IF YOU MANUALLY INPUT YOUR NUMBERS!!!! BUT THIS IS WHY I HATE HACKERRANK AND THEY DIDNT EXPLAIN...
    #HACKER RANK STARTED BY TELLING YOU INPUT CODE... YET EXPLAIN IN THE DESCRIPTION..... USE 3 & 5 !!!!! WHAT!?!?!?!?!?! 
#
#    

#Let's begin again to write it the hackerrank way - Using 3 & 5 per hacker rank request - Technically this is the answer.

if __name__ == '__main__':
    a = int(3)
    b = int (5)
    print(a + b)
    print(a - b)
    print(a * b)
