# functions or part of code used to do specific task
#inbuit functions
#user define functions

#inbuit functions
print()
range()
input()

#user define functions

#to define a function "def" is used

def add(a, b):
    result = a + b
    print("The sum is:", result)

# to call the function
add(5, 10)


#Program to find product (multiplication)

def multiply(a, b):
    return a * b

# user input
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

result = multiply(x, y)
print("The product is:", result)

#Program to check even or odd

def check_even_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

# user input
num = int(input("Enter a number: "))

result = check_even_odd(num)
print("The number is:", result)
