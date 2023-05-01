# 1. Write a program to print “Bright IT Career” ten times using for loop

from tkinter import N 

# Declaring variable

a = "Bright IT Career"
for i in range(10):
    print(a)


# 2. Write a program to print 1 to 20 numbers using the while loop

i = 1
while i <= 20:
    print(i)
    i += 1

# 3. Program to equal operator and not equal operators

a = 5
b = 10
print(a == b)
print(a != b)

# 4. Write a program to print the odd and even numbers.

numbers = [1,2,3,4,5,6,7,8,9,10]
# for even numbers
for i in numbers:
    if i % 2 == 0:
        print(i)

# for odd numbers
for i in numbers:
    if i % 2 != 0:
        print(i)

# 5. Write a program to print largest number among three numbers.

a = 15
b = 78
c = 45
if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c
print("The largest number: ", largest)


# 6. Write a program to print even number between 10 and 20 using while

a = 10
b = 20
print("Even number between 10 to 20: ", end = " ")
while a <= b:
    if(a % 2 == 0):  # if you find odd number between 10 to 20 then (a % 2 != 0)
        print("{0}".format(a), end = " ")
    a = a + 1
print()

# 7. Write a program to print 1 to 10 using the do-while loop statement.

a = 1
print("Print 1 to 10 using the the do-while loop statement: ", end = " ")
while True:
    print(a, end = " ")
    a = a + 1
    if(a > 10):
        break
print()

# 8. Write a program to find Armstrong number or not

i = int(input("Enter a number to cheak for armstrong: "))
sum = 0
orig = i
while i > 0:
    sum = sum + (i % 10) * (i % 10) * (i % 10)
    i = i // 10
if orig == sum:
    print("Armstrong number")
else:
    print("Not Armstrong number")

# 9. Write a program to find the prime or not.

n = int(input("Enter a Number to cheak for Prime: "))
count = 0 
i = 1
while i <= n:
    if n % i == 0:
        count += 1
    i += 1
if count == 2:
    print("Prime number")
else:
    print("Not prime number")


# 10. Write a program to palindrome or not.

n = int(input("Enter a number: "))
x = n 
r = 0
while n > 0:
    digit = n % 10
    r = r * 10 + digit
    n = n // 10
if x == n:
    print("Palidrome number")
else:
    print("Not palidrome")

# 11. Program to check whether a number is EVEN or ODD.

n = int(input("Enter a number: "))
if n % 2 == 0:
    print("Even number")
else:
    print("Odd number")

