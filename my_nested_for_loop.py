def printWordList():
  word = ["Apples","Bananas", "Pears","Carrots"]
  for outside in word:
    for inside in word:
      print(outside, inside)

printWordList()
