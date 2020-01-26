'''
A lambda function is a small anonymous function.

A lambda function can take any number of arguments, but can only have one expression.

Syntax:
lambda arguments : expression
'''

sum = lambda arg1,arg2 : arg1+arg2

print(sum(5,6))

#lambda function
def myFunction(n):
    return lambda a:a*n

doubler = myFunction(2)
tripler = myFunction(3)

print(doubler(3))
print(tripler(3))
