word=input("Enter the word:") #inputs the word
word=word.lower() #converts the word to lower so that there would be no dispreancy
if(word==word[::-1]): # checks the entered word and the word from last to first is same 
    print(f"{word} is a palindrome\n")
else:
    print(f"{word} is not a palindrome\n")

