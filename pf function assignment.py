# Question No: 1 
# Develop a program for an online shopping card
cost = 0
for i in range (3):
    quantity = int(input("Enter quantity:"))
    price = int(input("Enter price:"))
    total = quantity*price
    cost += total 
    print("total cost is:",cost)
    if 100 < cost < 200:
        discount = cost * 0.05
        total = cost - discount
        print("total amount is:",total)
    elif cost > 200:
        discount = cost * 0.1
        total = cost - discount
        print("total amount is:",total)
        break

# Question No: 2
# write a program for temperture converter   
temp = int(input("enter temperature:"))
if temp <= 0:
    print("wear warm clothes")
if temp >= 30:
    print("stayting hydrated") 

# Question No: 3
l1 = [ ]
for i in range (3):
    name = input("Enter names:")
    l1.append(name)
    print(l1)
if "kalsoom" in l1:
    print("yes") 

# Question No: 4
def factorial (num):
    factorial = 1
    i = 1
    while i <= num:
        factorial *= i
        i += 1
        print(factorial)
factorial (num) 
num = int(input("Enter number:"))

# Question no: 5
def is_palindrome(word):
    word = ''.join(char.lower() for char in word if char.isalnum())
    return word == word[::-1]

result1 = is_palindrome("level")
result2 = is_palindrome("python")

print(f"{'level'} is a palindrome: {result1}")
print(f"{'python'} is a palindrome: {result2}")

# Question No: 7
def generate_squares(n):
    return [i ** 2 for i in range(1, n + 1)]

def filter_even_squares(squares):
    return [square for square in squares if square % 2 == 0]

squares_list = generate_squares(10)

even_squares = filter_even_squares(squares_list)

print("List of Squares:", squares_list)
print("Even Squares:", even_squares)

# Question No: 8  
a = 5
b = a + 2
c = b * 3
print(c)
# output
# 21

x = 10
y = 3
result = x//y + x % y
print(result)
# output
# 4

for i in range(5):
    if i == 3:
       break
    print(i) 
# output
# 0
# 1 
# 2

my_list = [1,2,3]
my_tuple = tuple(my_list)  
print(my_tuple) 
# output
# (1,2,3)

student_info = {'name':'alice','age':20,'grade':'A'} 
print(student_info['age']) 
# output
# 20

def square(x):
    return x ** 2

result = square (4)
print(result)  
# output
# 16

num1 = 7
num2 = 3
result = num1 % num2 
print(result)
# output
# 1

value = 2**3*2
print(value)
# output
# 16

x = 15
if x > 10 and x % 2 == 1:
    print("Odd and greater than 10")  
else:
    print("Not meeting criteria")  
# output
# Odd and greater than 10

for i in range(2,8,2):
    print(i)
# output 
# 2
# 4            
# 6
