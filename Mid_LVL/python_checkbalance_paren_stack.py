#srbridge.com
#https://github.com/srbridgecom
#https://www.facebook.com/srbridge
#https://www.linkedin.com/in/r-bridge-3baa332a4/
#Python

#write a program to find whether a string has balanced parentheses or not.
#idea, use stack, when open, push it in a stack, when closed match the top of the stack and pop it
#if empty stack, return balance otherwise unbalanced.

open_list = ["[","{","("]
close_list = ["]","}",")"]

#function to check parenthesis
def check_func(theString):
    stack = []
    for i in theString:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if ((len(stack) > 0) and
                    (open_list[pos] == stack[len(stack)-1])):
                    stack.pop()
            else:
                return "Unbalanced"
    if len(stack) == 0:
        return "Balanced"
    else:
        return "UnBalanced"

#operation code

#balanced code
string = "{[]{()}}"
print(string,"-", check_func(string))

#unbalanced code
string = "[{}{})(]"
print(string,"-", check_func(string))

#return otherwise unbalance
string = "((()"
print(string, "=",check_func(string))
