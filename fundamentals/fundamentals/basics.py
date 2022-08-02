for i in range (1,151):
    print(i)


count = 0 
while count <= 15:
    print(count)
    count += 1


for i in range(0,1001,5):
    print(i)

count = 0 
while count <= 1000:
    print(count)
    count += 5 

for i in range(100):
    if i % 5 == 0:
        print("Coding")
    else:
        print(i)

count = 0

while count <= 100:
    if count % 5 == 0:
        print("Coding")
    else:
        print(count)
    count += 1

# Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.

Oddtotal = 0 
for i in range(1,500000):
    if(i % 2 != 0):
        Oddtotal = Oddtotal + i
print(Oddtotal)


count = 0 
Oddtotal = 0

while count <= 500000:
    if(count % 2 != 0):
        Oddtotal = Oddtotal + count
    count += 1

print(Oddtotal)

count = 2018

while count >= 0:
    print(count)
    count -= 4

for i in range(2018,0,-4):
    print(i)

lowNum = 2
Highnum = 9
mult = 3

for i in range(lowNum,Highnum+1):
    if(i % mult == 0):
        print(i)

