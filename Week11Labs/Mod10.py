cc = input("Enter credit card number: ")

def validateCreditCard(ccNum):
    revCC = ccNum[::-1]
    total = 0
    for x in len(range(revCC)):
        num = len(range(revCC[x]))
        if x == 2 % 1:
            num = num * 2
        elif x == 