###Variables - A python variable is a reserved memory location to store values.

##Declaring variables
#You don't need to declare variable type before using them in Python

year = 2022     #Here year is the variable name and 2022 is the asigned value
print(year)

#Output will be: 2022

#You can re-declare the variable even after you have declared it once

car = 2022
car = "red"     #Here we are re-declaring the value of the variable
print(car)

#Output will be: red

##Variable naming convention

# 1. Python is case sensitive
CAR = "Lamborgini"
car = "red"
print(car)
#Outpur will be: red

# 2. Begin with lowercase letters
firstName = "Sabbir"
first_name = "Sabbir"
#Avoid declaring variable this way: "First_name or FirstName"

# 3. Use "_" between the words in a variable
first_name = "Sabbir"
#Avoid declaring variable this way: "first name", "first+name", "first-name", "ID#" etc. If you give spaces or any other special signs between words in variable it will give erros.

# 4. Never start a variable name with digits (10first_name) or dollar signs ($first_name). Otherwise this will give errors.

#5. Variable names cannot be a reserved keyword. Example: and, del, while, in, print etc.

#Some of the best practice while naming variables:
#1. Have to be meaningful with the data stored in it.
#2. Cannot be too lenghty and too general, need to have a balance.
#3. Should not be written with single alphabets


#################################################


###Data types: Every value in Python has a Data type.
#1. Numeric - Integer, Float, Complex number
#2. Sequence - String, List, Tuple 
#3. Boolean - Data with one of the two build-in values True or False
#4. Dictionary - Unorderd collection of data in a key:value pair form
#5. Set - Ordered collection of data.

##type() function
#To know the data type of a variable we can just use type(variable_name)

x = 5
y = "Hello World"
z = [1, 2, 3, "Start"]

print(type(x))
print(type(y))
print(type(z))

#Output will be:
# <class 'int'>
# <class 'str'>
# <class 'list'>


#################################################


###Operators

##Arithmetic Operators

#Addition - Adds values on either side of the operator
x = 5
y = 2
print(x+y)
#Output will be: 7

#Substaction - Subtracts right hand operand from left hand operand
x = 5
y = 2
print(x-y)
#Output will be: 3

#Multipication - Multiplies values on either side of the operator
x = 5
y = 2
print(x*y)
#Output will be: 10

#Division - Divides left hand operand by right hand operand
x = 10
y = 4
print(x/y)
#Output will be: 2.5

#Modulus - This operator is also known as reminder operator
x = 10
y = 5
print(x%y)
#Output will be: 0

x = 10
y = 3
print(x%y)
#Output will be: 1

#Exponentiation - Performs exponential (power) calculation on operators. Power operator.
x = 3
y = 2
print(x**y)
#Output will be: 9

#Floor division - The real floor division operator is "//". It returns floor value for both integer and floating point arguments.
5//2 #Output will be: 2
-5//2 #Output will be: -3
2.0//2 #Output will be: 1.0
-5.0//2 #Output will be: -3.0

##Assignment Operators
x = 7  #Same as x = 7 #Assigns the value found in the right operand to the value found in the left operand
print(x) #Output will be: 7

y = 3
y += 5 #Same as y = 3 + 5 #Adds the value found in the right operand to the value found in the left operand
print(y) #Output will be: 8

z = 9
z -= 5 #Same as z = 9 - 5 #Substracts the value found in the right operand from the value found in the left operand
print(y) #Output will be: 4

p = 3
p *= 5 #Same as p = 3 * 5 #Multiplies the value found in the right operand by the value found in the left operand
print(p) #Output will be: 15

q = 10
q /= 5 #Same as q = 10 / 5 #Divids the value found in the left operand by the value found in the right operand
print(q) #Output will be: 2

##Identify Operators

#is - Returns True if both variables are the same object (Should be matched the data types)
x = 5
y = 5
print(x is y)
#Output will be: True

x = 5
y = 3
print(x is y)
#Output will be: False 

x = 5
y = "5"
print(x is y)
#Output will be: False (Although both of the value is 5 but y is a string and x is a number)

#is not - Returns True if both variables are not the same object (Should be matched the data types)

x = 5
y = 3
print(x is not y)
#Output will be: True

x = 5
y = 5
print(x is not y)
#Output will be: False

##Membership Operators

#in - Returns True if a sequence with the specified value is present in the object
x = "Hello World"
print('H' in x)
#Output will be: True

x = "Hello World"
print('S' in x)
#Output will be: False

x = "Hello World"
print('h' in x)
#Output will be: False (Although there is a H in x but still the output is False. Because the H in x is in capital letter and we know python is case sensitive)

# not in - Returns True if a sequence with the specified value is not present in the object
x = "Hello World"
print('H' not in x)
#Output will be: False

x = "Hello World"
print('S' not in x)
#Output will be: True


#################################################


###Input function, Type Convertion and Comments
##input() function - The simplest way to take input from the user is imput("prompt") -> It will read line from keyboard.
##input() pauses program execution to allow the user to type in a line of input from the keyboard. Once the user presses the Enter key, all charecters typed are read and returned as a "String".

name = input("Enter your name: ")
#Enter your name: Sabbir
print(name)
#Output will be: Sabbir

##Limitation of input() function is it always returns a string. If you want a numeric type then you need to convert the string to the appropriate type with int(), float(), or str() which are built-in functions.
number = input("Enter a number: ")
#Enter a number: 5
print(type(number))
#Output will be: <class: 'str'> - Although 5 is an integer but the data type is showing its as a string

number = input("Enter a number: ")
number = int(number)
#Enter a number: 5
print(type(number))
#Output will be: <class: 'int'> - After changing the data type with int() function the data type is now showing integer

##Type Conversion (Casting)
x = int(1) #x will be 1
y = int(2.8) #y wil be 2
z = int("3") #y wil be 3
a = float(2) #y wil be 2.0
b = float("3") #y wil be 3.0
c = str(22.8) #y wil be "22.8"

##Comments - Comments starts with a #. As soon as python see a # in code it just ignores the line

#Why use comments?
#1. To explain the code
#2. Make the code more readable

#We are printing something
print("Python is Cool")
#Output will be: Python is Cool - It will just ignore the texts in # contained line


#################################################