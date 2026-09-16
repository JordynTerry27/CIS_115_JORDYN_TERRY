price = float(input("Enter original price: "))

sales_tax = float(input("Enter sales tax: "))

sales_rate = sales_tax / 100

total = float(price * sales_rate)
print(total)



