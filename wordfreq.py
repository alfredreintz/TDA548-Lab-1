# Takes list of sentence as argument and returns the elements of the sentence as a list
def tokenize(lines):
    words = []

    for line in lines:
        # Remove the new line symbol at the end of every line
        # line = line.strip("\n")
        start = 0

        # Loops through the sentence        
        while start < len(line):
            # Excludes white spaces
            while start < len(line) and line[start].isspace():
                start += 1
             
            # Breaks the loop if index is out of range
            if start >= len(line):
                break
               
            # Check type of character
            if line[start].isdigit():
                startIndex = start

                # Loops until the type of character is not repeated
                while start < len(line) and line[start].isdigit():
                    start += 1

                # Adds the characters to the list
                words.append(line[startIndex : start])
            elif line[start].isalpha(): 
                startIndex = start

                while start < len(line) and line[start].isalpha():
                    start += 1
   
                words.append(line[startIndex : start].lower())
            else:
                words.append(line[start])
                start += 1
    
    # Return the list
    return words

# Function to sort out invalid words and count valid words
def countWords(words, stopWords):
    frequencies = {}                              
    #Code block that checks if the word is in stopWords, if it's not: 
    #get the value from the dictionary of the word, and add 1 to it.
    for i in words:
        if i not in stopWords:                  
            frequencies[i] = frequencies.get(i, 0) + 1  
        #If the word happens to be in stopWords, just skip it with 'continue'                                        
        else:
            continue                                  
    return frequencies    

# Function to print a the top n most used words from a dictionary
def printTopMost(frequencies,n):
    # Sort the dictionary into a list of tuples, high values to low values
    sort_list = sorted(frequencies.items(), key=lambda x: -x[1])

    # Loop through the sorted list up to n (or the end of the list)
    for word,freq in sort_list[:n]:
        print(word.ljust(20) + str(freq).rjust(5))