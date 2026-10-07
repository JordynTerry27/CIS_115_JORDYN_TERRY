month = input("Enter month: ")

def search(month):
    months = ["January","February","March","April","May","June","July","August","September","October","November","December"]
    if month in months:
        print(f"We found {month} in the months list. Search successful!")
    else:
        print(f"We cold not find {month} in the months list.")

search(month)