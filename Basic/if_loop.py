'''
Types of Operator
Python language supports the following types of operators.
    Arithmetic Operators
    Comparison (Relational) Operators
    Assignment Operators
    Logical Operators
    Bitwise Operators
    Membership Operators
    Identity Operators

'''


var1 = 100
if var1:
   print("1 - Got a true expression value")
   print(var1)

x=10
y=20
if x>y:
   print("max is ",x)
else:
   print("max is ", y)

var = 100
if(var>100):
   print("> 100")
elif(var > 200):
   print("> 200")
else:
   print("Larger no")

print("End of if")

'''
loop - while, for
'''
count = 0
while (count < 9):
   print( 'The count is:', count)
   count = count + 1
print("End of while")

#Using else Statement with Loops
count = 0
while count < 5:
   print( count, " is  less than 5")
   count = count + 1
else:
   print( count, " is not less than 5")

# Single Statement Suites
flag = 0
while (flag): print ('Given flag is really true!')
print( "Good bye!")

'''
for loop
'''
for letter in 'Python':     # First Example
   print ('Current Letter :', letter)

fruits = ['banana', 'apple',  'mango']
for fruit in fruits:        # Second Example
   print ('Current fruit :', fruit)

print ("Good bye!")

fruits = ['banana', 'apple',  'mango']
for index in range(len(fruits)):
   print ('Current fruit :', fruits[index])

print ("Good bye!")

for num in range(10,20):     #to iterate between 10 to 20
   for i in range(2,num):    #to iterate on the factors of the number
      if num%i == 0:         #to determine the first factor
         j=num/i             #to calculate the second factor
         print( '%d equals %d * %d' % (num,i,j))
         break #to move to the next number, the #first FOR
   else:                  # else part of the loop
      print (num, 'is a prime number')


#nested loop
i = 2
while(i < 100):
   j = 2
   while(j <= (i/j)):
      if not(i%j): break
      j = j + 1
   if (j > i/j) : print( i, " is prime")
   i = i + 1

print( "Good bye!")

# break statement
for letter in 'Python':     # First Example
   if letter == 'h':
      break
   print( 'Current Letter :', letter)

# continue statement
for letter in 'Python':     # First Example
   if letter == 'h':
      continue
   print ('Current Letter :', letter)

# pass statement
'''
It is used when a statement is required syntactically but you do not want any command or code to execute.

The pass statement is a null operation; nothing happens when it executes. The pass is also useful in places where your code will eventually go, but has not been written yet (e.g., in stubs for example) −
'''
for letter in 'Python':
   if letter == 'h':
      pass
      print( 'This is pass block')
   print ('Current Letter :', letter)

print ("Good bye!")
