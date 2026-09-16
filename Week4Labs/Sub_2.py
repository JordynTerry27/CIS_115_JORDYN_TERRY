num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

difference = num1 - num2

if difference < 0:
    print("Invalid! The value is less than zero.")
else:
    print("The values entered were valid integers.")