def validateCreditCard(ccNum):
    revCC = ccNum[::-1]
    total = 0
   
    
    for position in range(len(revCC)):
        number = int(revCC[position])
        
        
        if position % 2 == 1:
            number = number * 2
            if number > 9:
                number = number - 9
        total += number
    return total % 10 ==0 

while True:
    cc = input("Enter your credit card number: ") 
    if validateCreditCard(cc):
        print(f"The credit card number {cc} is valid!")
        break
    else:
        print(f"invalid credit card entered. Please try again.")


    
                
        
