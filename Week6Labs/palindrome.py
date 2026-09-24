string = input("Enter a word that is atleast five characters long: ")
def isPalindrome():
     palindrome = string[::-1]
     if string == palindrome:
          print(f"The string{palindrome} is a Palindrome.")
          return True
     else:
          print(f"The string{palindrome} is NOT a palindrome.")
          return False

isPalindrome()

        
    