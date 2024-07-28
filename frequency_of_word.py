import collections # importing the collections module
def count_word_frequencies(text): # defining the user defined function
    word=text.split() # using split function to split the words in a given text
    word_frequencies=collections.Counter(word) # using counter function in collections module
    return word_frequencies
text=input("Enter the text:")
frequencies=count_word_frequencies(text) #function calling
print("the word frequencies in a given text is:",frequencies)



