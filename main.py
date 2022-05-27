# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

#ASSIGNING THE FILE TO A VARIABLE
story = open("C:/Users/USER/Documents/Zuri Training/Python/Reading-Text-Files/story.txt", "r")

#DECLARING A FUNCTION WITH THE VARIABLE AS THE ARGUMENT
def read_file_content(story):
    
    print ("File has been read")
    
#DECLARING A FUNCTION THAT COUNTS THE WORDS IN THE FILE AND PRINTS A DICTIONARY
def count_words():
    #Calling the function for the file
    read_file_content(story)

    import string
    # Create an empty dictionary
    d = dict()

    # Looping through each line of the file
    for line in story:
        # Removing the spaces
        line = line.strip()

        # changing words to lowercase to avoid case mismatch
        line = line.lower()

        #Removing the punctuation marks from the line
        line = line.translate(line.maketrans("", "", string.punctuation))

        # Split the line into words
        words = line.split(" ")

        # Iterate over each word in line
        for word in words:
            # Check if the word is already in dictionary
            if word in d:
                # Increment count of word by 1
                d[word] = d[word] + 1
            else:
                # Add the word to dictionary with count 1
                d[word] = 1

    # Print the contents of dictionary
    for key in list(d.keys()):
        print(key, ":", d[key])


        # [assignment] Add your code here

        #return {"as": 10, "would": 20}
    #Open the file in read mode


#def count_words():
#    read_file_content()


count_words()