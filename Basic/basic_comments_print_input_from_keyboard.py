#Single line comment here

'''
Multiline comments here
line1
line2
and so on
'''

print("Pintu Gorai")
print("Line-1")
print("Line-2")
#python print without newline
print("Line-3",end=" ")
print("Line-3.1",end=' ')
print("Line-4")

print("hello","world")  #by default seperator is single space
print("hello","world",sep="")  #no seperator
print("hello","world",sep="   ") #seperator is three space



#Vaiables
vInt = 1
vFloat = 2.5
vString = "Pintu Gorai"
print("Values of vInt = ", vInt)
print("Values of vFloat = ", vFloat)
print("Values of vString = ", vString)

a,b,c=10,20.50,"Durgapur"
print("Values of a = ", a)
print("Values of b  = ", b)
print("Values of c = ", c)

x=2//3;
y=2/3;
print("x= 2//3 = ",x)
print("y= 2/3 = ",y)

m=max(x,2,3)
min = min(x,3,2,4)
print("max = ", m)
print("min = ",min)

'''
input from keyboard.
'''
print("Please enter a number : ")
x=input();
y=input("Please endter a number: ")

print("x = ", x)
print("y = ",y)

sum = int(x) + int(y)
print('Sum= ',sum)
