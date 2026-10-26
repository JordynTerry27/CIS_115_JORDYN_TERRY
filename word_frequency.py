sentence_input = input("Enter a sentence:")

def word_frequency(sentence):
  words = sentence.split()
  frequency = {}
  for word in words:
    if word in frequency:
      frequency[word] += 1
    else:
      frequency[word] = 1
   return frequency

final = word_frequency(sentence_input)
print(f"{final}")



      


 
