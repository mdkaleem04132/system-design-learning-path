#loops in python
#while loop
#for loop

i = 1
while i <= 10:
    print(i)
    i += 1

#with user input

nums = int(input("Enter a number: "))

i = nums
while i <= 5:
    print(i)
    i += 1   # important: update i

#sum of first 5 naturals num with while loop
i = 1
sum = 0

while i <= 5:
    sum += i
    i += 1

print("Sum of first 5 natural numbers is:", sum)


#for loop

i = 1
sum = 0
while i <= 5:
    sum += i
    i += 1
    print("Sum of first 5 natural numbers is:", sum)

for i in range(1, 6):
    print(i)

#sum of n naturals numbers
nums = int(input("Enter a number: "))
i = nums
sum = 0
while i <= 5:
    sum += i
    i += 1
    print("Sum of first 5 natural numbers is:", sum)
