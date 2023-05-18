import random
#What's a Variable??

"""Variable are containers for storing data values
"""

#python has no command for declaring a variable.

#When i call this is variable
"""
A variable is created the moment you first assign a value to it.
"""
#Example

x= 5
y='john'

print(x);

#Casting
#If you want to specify the data type of a variable, this can be done with casting.

#Example

l=str(3)
d=int(3)
f=float(3)

#How to get type of the variable??
#You can get the data type of a variable with the type() function.

print(type(l), type(d), type(f))


#Case-Sensitive
#Variable names are case-sensitive.

a = 4
A = "Sally"
#A will not overwrite a



#Python Variables - Assign Multiple Values

#1.Many Values to Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#2.One Value to Multiple Variables

a=b=c='readul'
print(a, b, c)

#unpacking

fruits=['apple','orange', 'banana'];
q,w,e=fruits;

print(q,w,e)

def myFnc():
    global q
    p='Name'
    q=1
    print('python is ', q)
    
    
    
myFnc()    

print(q)


# Data Types


string = str('hello str')
integer = int(3)
floatInteger = float(20.5)
complexType= complex(1j)
listType= list(('apple','banana', 'cherry'))



print(random.randrange(0,100*100))


# Loping Through a string

student = 'Ak.Mahamud'
print(student[len(student)-1])

for x in student:
    print(x)
    
    
    
boys=['ak', 'md', 're', 'cd'] 
print(len(boys),'boys')   


for x in boys:
    print(x)
    

print('ac' in boys) 



if 'ac' not in boys:
    print('you true')   