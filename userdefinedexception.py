# Program to demonstrate different built-in exceptions

try:
    print("----- Exception Handling Program -----")

    # 1. ZeroDivisionError
    a = 10
    b = 0
    print(a / b)

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

try:
    # 2. ValueError
    num = int("abc")
    print(num)

except ValueError:
    print("Error: Invalid value. Cannot convert text into integer.")

try:
    # 3. TypeError
    result = 10 + "20"
    print(result)

except TypeError:
    print("Error: Cannot add integer and string.")

try:
    # 4. IndexError
    numbers = [10, 20, 30]
    print(numbers[5])

except IndexError:
    print("Error: List index is out of range.")

try:
    # 5. KeyError
    student = {"name": "Rahul", "age": 20}
    print(student["marks"])

except KeyError:
    print("Error: Key does not exist in dictionary.")

try:
    # 6. FileNotFoundError
    file = open("abc.txt", "r")
    file.close()

except FileNotFoundError:
    print("Error: File not found.")

try:
    # 7. NameError
    print(student_name)

except NameError:
    print("Error: Variable is not defined.")

try:
    # 8. AttributeError
    number = 10
    number.append(20)

except AttributeError:
    print("Error: Object does not have this attribute.")

print("Program completed successfully.")