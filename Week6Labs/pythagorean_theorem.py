import math
x = float(input("Enter a value for x: "))
y = float(input("Enter a value for y: "))

def hyp(x,y):
    c = ((x ** 2) + (y ** 2)) ** 0.5 
    print(f"{c} is the hypotenuse.")
    return

hyp(x,y)