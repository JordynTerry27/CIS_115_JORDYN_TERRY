empty_list = []
initial_val = input("Enter intial value: ")

def append_to_list(item, target_list):
    empty_list.append(initial_val)

    while True:
        answer = input("Would you like to enter a value to append to the list? (y or n): ")
        if answer == "y":
            next_val = input("Enter next value: ")
            empty_list.append(next_val)
        elif answer == "n":
            print(f"{empty_list}")
            return
        elif answer != "y" or "n":
            print(f"Sorry, you have entered an invalid value, please try again")

append_to_list(initial_val, empty_list)


        





        

    
