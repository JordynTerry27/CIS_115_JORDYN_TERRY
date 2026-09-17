value = int(input("Enter an integer value between the range 0 and 100: "))
while value >= 0 and value <= 100:
    print(f"{value} is within range.")
    value = int(input("Enter another value between the range 0 and 100: "))
   
               
else:
    print("Sorry, the number you entered is out of range!")