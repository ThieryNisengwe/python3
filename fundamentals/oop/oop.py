class Human:
    planet = "Earth"
    def __init__(self,first_name,last_name,age,gender,height,weight,health=100):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.height = height
        self.weight = weight
        self.health = health
    def say_name(self):
        print(f"My name is {self.first_name} and {self.last_name}")
    def change_weight(self,amount:int, direction):
        if direction == 'up':
            self.weight += amount
        else:
            self.weight -= amount
        return self
    
    def info(self):
        print("*"*80)
        print(f"first_name: {self.first_name}")
        print(f"last_name: {self.last_name}")
        print(f"age: {self.age}")
        print(f"gender: {self.gender}")
        print(f"height: {self.height}")
        print(f"weight: {self.weight}")
        print(f"health: {self.health}")
        return self
    
    def punch(self,person):
        person.health -= 1
        return self
    def change_health(self,amount):
        self.health += amount
        return self
    @classmethod 
    def change_planets(cls,planet):
        cls.planet = planet
        return cls
    @staticmethod
    def validator(data):
        is_valid = True
        if len(data['first_name'])< 1:
            print("You need a first name")
            
tyler = Human('tyler','tbo','33',"5'8\"",'male',180)
kyle = Human('kyle','marrymeee',27,"5'11\"",'male',200)

tyler.say_name()

print(tyler.weight)
tyler.change_weight(30,'up')
print(tyler.weight)

kyle.punch(tyler)

tyler.info()

print(tyler.planet)

Human.change_planets("simosis 1")
print(tyler.planet)
print(kyle.planet)

people = [
    {
        'first_name': 'tyler',
        'last_name': 'tbo',
        'age': '33',
        'height': "5'8\"",
        'weight':'180',
        'gender': 'male',
        'health': 100,
    }
        {
        'first_name': 'kyle',
        'last_name': 'marrymeee',
        'age': '27',
        'height': "5'11\"",
        'weight':'200',
        'gender': 'male',
        'health': 100
    }
]

all_people = []

for person in people:
    temp_rendered = Human(person)
    
    
