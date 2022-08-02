print(type(24))
print(type(3.9))
print(type(3j))

int_to_float = float(34)
float_to_int = int(30.1)
int_to_complex = complex(35)
print(type(int_to_float))
print(type(float_to_int))
print(type(int_to_complex))

import random
from re import X
from sys import last_traceback
from xml.dom.minicompat import EmptyNodeList

# print(random.randint(1,10))

for i in range(10):
    print(random.randint(1,10))
    
print("this is just a string")

name = "Zen"
print("My name is", name)

name = "Zen"
print("My name is " + name)

print("Hello" + 42)
print("Hello " + str(42))

total = 35 
user_val = int("26")

total = total + user_val

print(total)

first_name = "Zen"
last_name = "Coder"
age = 27

print(f"My name is {first_name} {last_name} and I am {age} years old.")

first_name = "Zen"
last_name = "Coder"
age = 27
print("My name is {} {} and I am {} years old.".format(first_name,last_name,age))
print("My name is {} {} and I am {} years old.".format(age,first_name,last_name))

x = "this is a test string for upper"

y = "THIS IS A TEST STRING FOR LOWER"

print(y.lower())
print(x.upper())
print(x.count("hello hello hello hello hello hello hello hello hello"))

ninjas = ['Rozen', 'KB', 'Oliver']
my_list = ['4', ['list', 'in', 'a', 'list',], 986]
empty_list = []

fruits = ['apple', 'banana', 'orange', 'strawberry',]
vegatibles = ['lettuce', 'cucumber', 'carrots']
fruits_and_vegatibles = fruits + vegatibles
print(fruits_and_vegatibles)
salad = 3 * vegatibles
print(salad)


# play around with the drawers!
drawers = ['documents', 'envelopes', 'pens']

# Print the second value from the list (envelopes)
print(drawers[1])

# Change "pens" to "useless manuals"
drawers[2] = "useless manuals"
# Change the first value to whatever is the second value
drawers[0] = drawers[1]
# What should the list look like now?
#[envelopes,envelopes,useless manuals]
# Print the list! Does it match your prediction?
print(drawers)


nums = [1,2,3,4,5]
nums.append(99)
print(nums)


words = ["start", "going","till","the","end"]
print(words[1:])
print(words[:4])
print(words[2:4])

copy_of_words = words[:]
copy_of_words.append("dojo")
print(copy_of_words)
print(words)