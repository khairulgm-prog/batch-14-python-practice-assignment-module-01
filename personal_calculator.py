#Practice Problem 1: Personal Information & Simple Calculator

#personal_calculator.py

#1.Ask the user for their name.

name=input(f"Enter your name:  ")

#2. Ask for their age.

age=input(f"Enter your age:  ")

#3. Ask for two numbers.

number1=float(input(f"Enter first number:"))
number2=float(input(f"Enter second number:"))

#4. Calculate the sum, subtraction, multiplication, and division of those two numbers.

add_number=number1 + number2
sub_number=number1 - number2
multipli_number=number1 * number2

# Handle division by zero safely
if number2 != 0:
    div_number = number1 / number2
else:
    div_number = "Undefined (Cannot divide by zero)"

#5. Display all information in a well-formatted output using f-strings.

print("")
print(f"Hello. {name}!")
print("")
print(f"Your age is {age}")
print("")

print(f"Addition: {add_number}")
print("")

print(f"Subtraction: {sub_number}")
print("")

print(f"Multiplication: {multipli_number}")
print("")

print(f"Division: {div_number}")
print("")

print("Md Khairul Alam Prodhan")