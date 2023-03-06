# print all integers from 0 to 150
for i in range(151):
    print(i)

# print all multiples of 5 between 5 and 1000 (inclusive)
for i in range(5,1001,5):
    print(i)

# print numbers 1 to 100, replacing multiples of 5 with 'Coding'
# and multiples of 10 with 'Coding Dojo' 
for i in range(1,101):
    if i % 5 == 0 and i % 10 != 0:
        print('Coding')
    elif i % 10 == 0:
        print('Coding Dojo')
    else:
        print(i)

# add all of the odd integers from 1 to 500000
sum = 0
for n in range(1,500001):
    if(n % 2 != 0):
        sum += n
print(sum)

# countdown from 2018 by 4s
for n in range (2018,1,-4):
    print(n)

# flexible counter
lowNum = 2
highNum = 9
mult = 3
for n in range(lowNum, highNum + 1):
    if(n % mult == 0):
        print(n)

