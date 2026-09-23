import math
x = float(input("Enter a value for x: "))
y = float(input("Enter a value for y: "))

def trig(y,x):
    theta = math.atan2(y,x) * (180 / 3.14)
    print(f"The angle theta is {theta}.")
    return

trig(x,y)
