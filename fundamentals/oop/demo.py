car = {
    'make': 'kia',
    'model': 'optima',
    'year': '2015',
    'color': 'Silver',
    'price': '$20,000',
}

class Saleman:
    all_salesmen = []
    def __init__(self,data):
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.job_title = data['job_title'] 
        self.sale_record = data['sale_record']
        self.salary = data['salary']
        Saleman.all_salesmen.append(self)
        
        def info(self):
            print("*"*80)
            print(f"first_name: {self.first_name}")
            print(f"last_name: {self.last_name}")
            print(f"job_title: {self.job_title}")
            print(f"sale_record: {self.sale_record}")
            print(f"salary: {self.salary}")
            return self

class Car:
    all_cars = []
    def __init__(self,data):
        self.make = data['make']
        self.model = data['model']
        self.year = data['year']
        self.color = data['color'] 
        self.price = data['price'] 
        Car.all_cars.append(self)

class Customer:
    all_customers = []
    def __init__(self,data):
        self.firsst_name = data['firsst_name']
        self.last_name = data['last_last']
        self.budget = data['budget']
        self.credit_rating = data['credit_rating']
        Customer.all_customers.append(self)

car_data = [
    {
        'make' : 'honda',
        'model' : 'civic',
        'year' : '2019',
        'color' : 'white',
        'price' : 19200,
    },
    {
        'make' : 'toyota',
        'model' : '4runner',
        'year' : '2022',
        'color' : 'grey',
        'price' : 63500,
    },
    {
        'make' : 'subaru',
        'model' : 'wrx',
        'year' : '2016',
        'color' : 'blue',
        'price' : 26900,
    },
    {
        'make' : 'mazda',
        'model' : 'cx5',
        'year' : '2018',
        'color' : 'red',
        'price' : 23000,
    }
]


salesman_list = [
    {
        "first_name": "john",
        "last_name": "smith",
        "job_title": "VP of Sales",
        "sale_record": 400,
        "salary": 67000,
    },
    {
        "first_name": "Mark",
        "last_name": "Anthony",
        "job_title": "SR Sales Associate",
        "sale_record": 125,
        "salary": 50000,
    },
    {
        "first_name": "Peter",
        "last_name": "Weller",
        "job_title": "Jr Sales Associate",
        "sale_record": 40,
        "salary": 35000,
    },
    {
        "first_name": "Keanu",
        "last_name": "Reaves",
        "job_title": "Jr Sales Associate",
        "sale_record": 53,
        "salary": 35000,
    }
]




customer_data = [
    {
        'first_name' : 'Tyler',
        'last_name' : 'tbo',
        'budget' : 65000,
        'credit_rating' : 790,
    },
        {
        'first_name' : 'Tom',
        'last_name' : 'Harris',
        'budget' : 250000,
        'credit_rating' : 850,
    },
]

for dictionary in car_data:
    Car(dictionary)
    
    
for dictionary in salesman_list:
    Saleman(dictionary)

for dictionary in customer_data:
    Customer(dictionary)