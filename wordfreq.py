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
                words.append(line[start])
                start += 1
    
    # Return the list
    return words

def countWords(words, stopWords):
    frequencies = {}

    for i in words:
        if i in stopWords:
            continue
        
        if i in frequencies:
            frequencies[i] += 1
        else:
            frequencies[i] = 1
    
    return frequencies

def printTopMost(frequencies, n):
    sortedFrequencies = sorted(frequencies.items(), key=lambda x: x[1])

    for i in sortedFrequencies:
        print(f"{i[0]}{i[1]}")