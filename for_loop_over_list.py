def getMyList():
  list = [10,20,30,40,50,60]
  counter  = 0
  for value in list:
    print(value)
    counter = counter + 1
  return counter 

total_loops = getMyList()
print(f"The loop iterated {total_loops} times.")
  

