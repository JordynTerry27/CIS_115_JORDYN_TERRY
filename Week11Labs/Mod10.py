cc = input("Enter credit card number: ")

def validateCreditCard(ccNum):
    revCC = ccNum[::-1]
    total = 0
    for position in len(range(revCC)):
        