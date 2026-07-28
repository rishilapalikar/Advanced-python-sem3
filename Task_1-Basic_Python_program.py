#Level 1: Basic Python Programming (Any 3)

#2. Add Two Numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

sum = num1 + num2

print("Sum =", sum)

#5. Check Even or Odd
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")

#7. Largest of Three Numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest =", a)
elif b >= a and b >= c:
    print("Largest =", b)
else:
    print("Largest =", c)

#Level 2: Conditional Statements (Any 3)

#11. Positive, Negative or Zero
num = float(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

#12. Leap Year
year = int(input("Enter year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not a Leap Year")

#14. Vowel or Consonant
ch = input("Enter a character: ")

if ch.lower() in ['a', 'e', 'i', 'o', 'u']:
    print("Vowel")
else:
    print("Consonant")

#Level 3: Loops (Any 2)

#18. Factorial
num = int(input("Enter a number: "))

fact = 1

for i in range(1, num + 1):
    fact *= i

print("Factorial =", fact)

#25. Prime Number
num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")
else:
    print("Not Prime")

#Level 5: Strings (Any 1)

#31. Reverse a String
text = input("Enter a string: ")

print("Reversed String:", text[::-1])

#Level 6: Lists (Any 1)

#39. Sort a List
numbers = []

n = int(input("How many elements? "))

for i in range(n):
    numbers.append(int(input("Enter element: ")))

numbers.sort()

print("Sorted List:", numbers)

#Level 7: Functions (Any 1)

#42. Function to Check Prime Number
def is_prime(num):
    if num <= 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True


number = int(input("Enter a number: "))

if is_prime(number):
    print("Prime")
else:
    print("Not Prime")

#Level 8: Dictionaries and Tuples (Any 1)

#46. Create and Display a Dictionary
student = {
    "Name": "Rishi",
    "Roll No": 31,
    "Course": "B.Tech"
}

print("Student Dictionary")

for key, value in student.items():
    print(key, ":", value)

#Level 9: File Handling (Any 1)

#51. Create and Write into a File
file = open("sample.txt", "w")

file.write("Welcome to Python File Handling.\n")
file.write("This is a sample file.")

file.close()

print("Data written successfully.")

#Level 10: Exception Handling (Any 1)

#56. Handle Division by Zero
try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))

    result = a / b

    print("Result =", result)

except ZeroDivisionError:
    print("Error! Division by zero is not allowed.")