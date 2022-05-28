# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

import string

#declaring a function for reading the file
def readFileContent(story):
    file = open("C:/Users/USER/Documents/Zuri Training/Python/Reading-Text-Files/story.txt", "r")
    thefile = file.read()
    return thefile
    

def count_words():
    text = readFileContent("C:/Users/USER/Documents/Zuri Training/Python/Reading-Text-Files/story.txt")
    
    #removing punctuations
    cleanText = text.translate(text.maketrans("", "", string.punctuation))

    #spliting the sentences into words
    splitText = cleanText.split()

   #making an empty dictionary then adding the words as keys and their count as values 
    countText = {}
    for word in splitText:
        if word in countText:
            countText[word] += 1
        else:
            countText[word] = 1
    return countText


print (count_words())