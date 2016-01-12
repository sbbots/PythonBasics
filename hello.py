import random
import sys
import os


print(" World")
name ="Sam"
print(name)

#Datatypes
# Numbers
# Strings
# Lists
# Tuples
# Dictionaries

#Arithmetic Operators
# +
# -
# *
# /
# %
# **
# //

print("5+2=", 5+2)
print("5-2=", 5-2)
print("5*2=", 5*2)
print("5/2=", 5/2)
print("5%2=", 5%2)
print("5**2=", 5**2)
print("5//2=", 5//2)
print("1+2-3*2 =" ,1+2-3*2)
print("(1+2-3)*2 =" ,(1+2-3)*2)

#String
qoute = "\"Always remember you are unique"
multi_line_qoute = ''' just
like everyone else'''

print("%s %s %s" %('I like the quite', qoute, multi_line_qoute))
print("\n"* 5)
print("I don't like ", end="")
print("newlines")

#Arrays
grocery_list = ['Juice', 'Tomatoes', 'Potatoes',
                'Bananas']
print('First Item', grocery_list[0])
grocery_list[0] = "Green Juice"
print('First Item', grocery_list[0])
print(grocery_list[1:3])
other_events = ['Wash', 'Pick Up Kids', 'Cash Check']
to_do_lists = [other_events,grocery_list]
print(to_do_lists)
print((to_do_lists[1][1]))
grocery_list.append('Onions')
print(to_do_lists)
grocery_list.insert(1, "Pickle")
print(to_do_lists)
grocery_list.remove("Pickle")
print(to_do_lists)
grocery_list.sort()
print(to_do_lists)
grocery_list.reverse()
del grocery_list[4]
print(to_do_lists)

to_do_lists2 = other_events + grocery_list

print(len(to_do_lists2))
print(max(to_do_lists2))
print(min(to_do_lists2))

#Tuples
pi_tuple = (3,1,4,1,5,9)
new_tuple = list(pi_tuple)
new_list = tuple(new_tuple)
print(len(new_tuple))
print(min(new_tuple))
print(max(new_tuple))

#Dictionary

super_villians = {'Fiddler' : 'Isaac Bowin', 'Captain Cold' : 'Leonard Snart', 'Weather Wizard': 'Mark Mardon'}
print(super_villians)
print(super_villians['Captain Cold'])
del super_villians['Fiddler']
print(super_villians)
super_villians['Captain Cold'] = "a"
print(super_villians)
print(super_villians.get("Captain Cold"))
print(super_villians.keys())
print(super_villians.values())

#If Constructs
age = 21
if age > 16 :
    print("You are old enough to drive")
else :
    print('You are not old enough to drive')

if age >= 21 :
    print("You are old enough to drive a tractor")
elif age >=16:
    print("You are old enough to drive")
else:
    print("You are not old enough")

# and or operators

if((age>=1) and (age<=18)):
    print("You get a birthday")
elif ((age==21) or (age >=65)) :
    print("You get a special birthday")
elif not(age == 30):
    print("You don't get a birthday")
else :
    print("You get a birthday party yeah")



# Loop constructs

#for
for x in range(0,10):
    print(x, ' ',end="")
for y in grocery_list:
     print(y)
for x in [2,4,6,8,10]:
    print(x)
num_list = [[1,2,3], [10,20,30],[100, 200, 300] ]
for x in range(0,3):
    for y in range(0,3):
        print(num_list[x][y])
# while

random_num = random.randrange(0,100)
while(random_num!=15):
    print(random_num)
    random_num = random.randrange(0,100)

#while 2
i=0
while(i<=20):
     if(i%2==0):
         print(i)
     elif(i==9):
         break
     else:
         i += 1
         continue
     i+=1

## Functions

def addNumber(fNum, lNum):
    sumNum = fNum+lNum
    return sumNum

print("Sum is ", addNumber(1,4))
print('What is your name')
name = sys.stdin.readline()
print("a ",name)

long_string = "I'll catch you if you fall - The Floor"

print(long_string[0:4])
print(long_string[-5])
print(long_string[:4] + " be there")
print("%c is my %s letter and my number %d number is %.5f" %
      ('X','favorite', 1, .14))
print(long_string.capitalize())
print(long_string.find("ll"))
print(long_string.isalnum())
print(long_string.isalnum())
print(long_string.replace("Floor", "Ground"))
print(long_string.strip())
qoute_list = long_string.split("l")
print(qoute_list)

## IO Operations

test_file = open("test.txt", "wb") # for read use ab+ to read and append to the file, it creates the file
print(test_file.mode)
print(test_file.name)
test_file.write(bytes("Write me to the file\n", "UTF-8"))
test_file.close()
test_file = open("test.txt", "r+")
print(test_file.read())
os.remove("test.txt")

#Comment
