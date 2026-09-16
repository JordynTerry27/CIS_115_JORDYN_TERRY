num = int(input("Enter # of grades up to 10: "))

counter = 0

while counter < num:
    counter = counter + 1
    grade = int(input("Enter grade: "))
    print(grade)
else: 
    print(f"The user has entered {counter} grades.")


