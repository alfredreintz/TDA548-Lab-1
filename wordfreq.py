# Takes list of sentence as argument and returns the elements of the sentence as a list
def tokenize(lines):
    words = []

    for line in lines:
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
                startIndex = start

                while start < len(line) and not line[start].isalpha() and not line[start].isdigit() and not line[start].isspace():
                    start += 1

                words.append(line[startIndex : start])
    
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

def printTopMost(frequencies, n):
    sortedFrequencies = sorted(frequencies.items(), key=lambda x: -x[1])

    # Loop n times if n is less than the length of the list, otherwise loop the length of the list times
    for i in range(n) if n <= len(sortedFrequencies) else range(len(sortedFrequencies)):
        # Using string formatting methods for the alignment of the output
        # An alternative would be to use :<20 for the word and :>5 for the numbers
        print(f"{sortedFrequencies[i][0].ljust(20)}{str(sortedFrequencies[i][1]).rjust(5)}")