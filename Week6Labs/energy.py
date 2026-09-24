import math

c = 2.99 * (10 ** 8)
m = float(input("Enter mass: "))
def calculate_energy(m):
    e = (m * c) ** 2
    print(f"The energy produced is {e} Joules")
    return

calculate_energy(m)