#1
def number_of_food_groups():
    return 5
print(number_of_food_groups())
#print 5 because the number of food groups becomes "5"

#2
def number_of_military_branches():
    return 5
# print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
# doesn't work because number_of_days_in_a_week_silicon_or_triangle_sides is not defined
#so we get an error here

#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())
# we will get 5 because the return statements also ends the function.
# so it will print 5 


#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())
# will also print 5 because the return statements ends the function before the print statement gets executed

#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)
# will return nothing because the print statement doesn't store the value x it just prints it 
# it will print 5 first but then print nothing because number_of_great_lakes() has nothing to returned

#6
def add(b,c):
    print(b+c)
# print(add(1,2) + add(2,3))
# there's nothing returned so we can't add anything. 

#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))
# should print "25"

#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())
# will print 10 because the return is 10, ## will also print 

#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3)) # will print 7
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3)) # 14
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3)) # will return 21


#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))
# should print 8 


#11
b = 500
print(b) # will print 500 
def foobar():
    b = 300
    print(b)
print(b) # will print 500
foobar() # will print 300 since the function states b = 300 
print(b) # 500

#12
b = 500
print(b) # will print 500
def foobar():
    b = 300
    print(b)
    return b
print(b) # will print 500
foobar() # will print 300 since the function states b = 300
print(b) # will print 500


#13
b = 500
print(b) # will print 500
def foobar():
    b = 300
    print(b)
    return b
print(b) # will print 500
b=foobar() # will print 300 and then another 300 
print(b) # will print 500 so we should see 500,500,300,300,500


14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()
# 1,2,3

#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)

# 1,3