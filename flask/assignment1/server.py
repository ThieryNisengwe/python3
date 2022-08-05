from flask import Flask, render_template
app = Flask(__name__)
# THIS WILL MOVE !!!.


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/whateveryouwant/<name>/<int:id>')
def whateveryouwant(name, id):
    print(name)
    print(id)
    return render_template('page2.html')


@app.route('/another function')
def anotherfunction():
    return'something'


@app.route('/add_two_vals/<int:num1>/<int:num2>')
def add_two_vals(num1, num2):
    sum = num1+num2
    print("{num1}+{num2}={sum}")
    return render_template('page3.html', num1=num1, num2=num2, sum=sum)


# END OF MOVING-CODE
# This must be at the bottom of the file
if __name__ == "__main__":
    app.run(debug=True)


class Saleman:
    def __init__(self, data):
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.job_title = data['job_title']
        self.sale_record = data['sale_record']
        self.salary = data['salary']


class Car:
    def _init_(self, data):
        self.make = data['make']
        self.model = data['model']
        self.year = data['year']
        self.color = data['color']
        self.price = data['price']


class Customer:
    def __init__(self, data):
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.budget = data['budget']
        self.credit_rating = data['credit_rating']
