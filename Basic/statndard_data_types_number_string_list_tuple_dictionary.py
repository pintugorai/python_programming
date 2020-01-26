'''
Standard Data Types:
    Numbers
    String
    List
    Tuple
    Set
    Dictionary
'''
# Numbers -
var1 = 1
var2 = 10
print("Var1= ", var1)
print("var2= ", var2)
#You can delete number Object using del.
del var1
#del var1,ver2
#print("var1 = ", var1) # Compile time error - NameError: name 'var1' is not defined
print("var2 = ", var2)

'''
Python supports four different numerical types −
    int (signed integers)
    long (long integers, they can also be represented in octal and hexadecimal)
    float (floating point real values)
    complex (complex numbers)
'''
i=1
l=123123213123
f=2.5
com1 = 10+12J
com2 =20j
com3 = 20 +0j
print(com1)
print(com2)
print(com3)

#Python Strings:
'''
Contiguous set of characters represented in the quotation marks.
The plus (+) sign is the string concatenation operator
The asterisk (*) is the repetition operator
Subsets of strings can be taken using the slice operator ([ ] and [:] ) with indexes starting at 0 in the beginning of the string and working their way from -1 at the end.

'''
s = "Pintu Gorai"
str = 'Pintu Gorai'
multilineString = """ Python multiline string always enclused in 
triple quote.
This is an example of multiline string."""
print("multilineString = ", multilineString)
print(str)
print(str[0])
print(str[2:5]) # Prints characters starting from 3rd to 5th
print(str[2:]) # Prints string starting from 3rd character
print(str * 2) # Prints string two times
print(str + ", Master in Computer Science")  # Prints string two times

#List
'''
Python Lists: compound data types. A list contains items of DIFFERENT data types separated by commas and enclosed within square brackets ([]).
Values can be accessed using the slice operator ([ ] and [:]) with indexes starting at 0 in the beginning of the list and working their way to end -1. 
The plus (+) sign is the list concatenation operator.
The asterisk (*) is the repetition operator.

'''
list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']

print (list)          # Prints complete list
print (list[0])     # Prints first element of the list
print (list[1:3]  )   # Prints elements starting from 2nd till 3rd
print (list[2:] )     # Prints elements starting from 3rd element
print (tinylist * 2  )# Prints list two times
print (list + tinylist) # Prints concatenated lists

myList=['Pintu',100,'Durgapur']
print("myList = ",myList)
#Accessing an element
print("myList[1]= ",myList[1])
print("myList[-2]= ",myList[-2])
#updating
myList[1]=200.00
print("myList = ",myList)
#Deleting element from list
del myList[2]
print("myList = ",myList)
import time
time.sleep(20)


#Tuple
'''
Python Tuples: A tuple is another sequence data type that is similar to the list. A tuple consists of a number of values separated by commas. Unlike lists, however, tuples are enclosed within parentheses.

The main differences between lists and tuples are: 
1. Lists are enclosed in brackets []
tuples are enclosed in parentheses ()
2. List: elements and size can be changed, 
 Tuples: cannot be updated. Tuples can be thought of as READ-ONLY lists. 
 
'''
tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
tinytuple = (123, 'john')

print(tuple)          # Prints complete list
print(tuple[0] )       # Prints first element of the list
print (tuple[1:3] )     # Prints elements starting from 2nd till 3rd
print (tuple[2:] )      # Prints elements starting from 3rd element
print (tinytuple * 2 )  # Prints list two times
print(tuple + tinytuple) # Prints concatenated lists

tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
list = [ 'abcd', 786 , 2.23, 'john', 70.2  ]
#tuple[2] = 1000    # Invalid syntax with tuple, because tuple is read only, cannot be change/update
list[2] = 1000     # Valid syntax with list


#set
'''
Set is a collection which is unordered and unindexed. No duplicate members.
'''
itemSet = {'dropbox','azure','aws'}
print("item set = ", itemSet)

#add one item to a set use the add() method
itemSet.add("newCloud")
print("item set = ", itemSet)

#Add multiple items to a set, using the update() method
itemSet.update(['Azure','Aws'])
print("item set = ", itemSet)

#length of set, len() method
print('length = ', len(itemSet))

#remove an item from set, using remove() and discard()
itemSet.remove('azure')
print("item set = ", itemSet)
itemSet.discard('aws')
print("item set = ", itemSet)
#If the item to remove does not exist, discard() will NOT raise an error.
#itemSet.remove('ItemNotExist') # ERROR
itemSet.discard('ItemNotExist')
print("item set = ", itemSet)
#pop() method will remove last item
itemSet.pop()
print("item set = ", itemSet)
#remove all items/clear all item using clear() method
itemSet.clear()
print("item set = ", itemSet)
#Delete set completely
del itemSet
#print("item set = ", itemSet)
#Join Two Sets
#Both union() and update() will exclude any duplicate items.
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)
set1.update(set2)
print(set1) 

#Dictionary
'''
Python's dictionary:
It is a kind of hash table type. 
Consist of key-value pairs. 
A dictionary key can be almost any Python type, but are usually numbers or strings. Values, on the other hand, can be any arbitrary Python object.

Dictionaries are enclosed by curly braces ({ }) and values can be assigned and accessed using square braces ([]).

'''
dict = {}
dict['one'] = "This is one"
dict[2]     = "This is two"

tinydict = {'name': 'john','code':6734, 'dept': 'sales'}
print(dict['one'])     # Prints value for 'one' key
print(dict[2])         # Prints value for 2 key
print(tinydict)        # Prints complete dictionary
print(tinydict.keys())  # Prints all the keys
print(tinydict.values()) # Prints all the values
