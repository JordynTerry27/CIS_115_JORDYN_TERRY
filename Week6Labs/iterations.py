val = int(input("Enter the amount of loops: "))

def print_iterations(val):
    counter = 0
    for x in range(val):
        counter = counter + 1
    return counter 

result = print_iterations(val)

print(f"The function call looped {result} times.")