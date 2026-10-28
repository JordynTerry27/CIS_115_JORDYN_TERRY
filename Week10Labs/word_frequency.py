user_sentence = input("Enter a sentence: ")

def word_frequency(sentence):
    words = user_sentence.split()

    frequency = {}

    for word in words:
        if word in words:
            frequency[word] += 1
        else:
            frequency[word]= 1

    return frequency


