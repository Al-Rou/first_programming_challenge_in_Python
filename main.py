#Prompting the user
enteredSentence = input("Enter your sentence: ")
words = ""
listOfWords = []
#Separating words and storing in an array
for i in range (len(enteredSentence)):
    if (enteredSentence[i] != ' '):
        words += enteredSentence[i]
    else:
        listOfWords.append(words)
        words = ""
listOfWords.append(words)
#Making the sentence backward
sentenceBackward = ""
for i in range (len(listOfWords)-1, -1, -1):
    sentenceBackward += listOfWords[i]
    sentenceBackward += " "
#Printing the result out
print(sentenceBackward)