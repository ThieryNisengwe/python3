

from audioop import add
from genericpath import exists


class Item:
    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the recived arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero !"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero !"

        # Assign to self.object
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity


item1 = Item("Phone", 100, -1)
item2 = Item("Laptop", 1000, -3)


print(item1.calculate_total_price())
print(item2.calculate_total_price())

first_name = "Thiery"
last_name = "Nis"
age = 34
message = "Hello my name is %s %s and I am years %d years old"%(first_name,last_name,age)
print(message)
message = "Hello my name is {} {} and I am years {} years old".format(first_name, last_name, age)
print(message)
message = f"Hello my name is {first_name} {last_name} and I am {age} years old"
print(message)


list_of_bros = ['tyler', 'joe',]

list_of_bros.append('billy bob')
list_of_bros.append(56)

list_of_bros[2] = 'curtis'
list_of_bros.append ('Joe shmo')

unwated_number  = list_of_bros.pop(3)

# prints only 'curtis'
print(list_of_bros)
print(list_of_bros[1:3])
print(unwated_number)

fullname = "Thiery Nis"

for char in fullname:
    print(char)

print(fullname[3])

person = ('Tyler', 'thibault')

list = []

for item in person:
    list.append(item)
    
list[0] = "joe"

print(person[0])
# print[list]

def some_func():
    some_list = ['Tyler,joe,curtis']
    for item in some_list:
        print(item)
        

some_func()


bros = ['tyler,joe,curtis']

for item in bros:
    if item == 'tyler':
        print("He is the best")
    elif item == 'joe':
        print("he is the middle and the trouble maker")
    else:
        print("This is an else statement")

for num in range(100):
    if num % 2 == 0:
        print("this is even")
    else:
        print("this is odd")




person = {
    'first_name': 'tyler',
    'last_name': 'tbo',
    'age': 33
}

print(person['last_name'])

person['first_name'] = "thiabult" 

person['fave_color'] = 'green'

person['fave_color2'] = 'blue'

print(person)

# 1 
# person.clear()
# 2
# thing_removed = person.pop('fave_color')

print(person)
# print(thing_removed)

# 3 
del person['fave_color']

brothers = [
    {
    'first_name': 'tyler',
    'last_name': 'tbo',
    'age': 33,
    'fav_color': ['green','black'],
    'car':{
        'make': 'GMC',
        'model': 'Sierra',
        'year': 2016,
    }
},
    {
    'first_name': 'joe',
    'last_name': 'tbo',
    'age': 33,
    'fave_color': ['green','white'],
},
    {
    'first_name': 'curtis',
    'last_name': 'tbo',
    'age': 33,
    'fave_color': ['blue'],
}
]

print(brothers[0]['fav_color'][0])
print(brothers[0]['car']['year'])


# for dictionary in brothers:
#     for key in dictionary:
#         print(key)




#parameters
def add_nums(num1=5, num2=7):
    return num1 + num2

#arguments
# print(add_nums(8,7))
# print(add_nums(82727,8))

print(add_nums())
print(add_nums(num1=10))

count = 0
while count <= 10:
    print("looping -", count)
    count -= 2

x = 12

if x > 50:
    print("bigger than 50")
else:
    print("smaller than 50")


x = 55
if x > 10:
    print("bigger than 10")
elif x > 50:
    print("bigger than 50")
else:
    print("smaller than 50")

if x < 10:
    print("Small than 10")


for i in range(5):
    print(i)

for i in range(2,8):
    print(i)

print(type(range(5)))

print(type(10))

