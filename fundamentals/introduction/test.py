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