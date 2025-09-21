def tokenize(lines):
    words = []
    for line in lines:
        start = 0
        
        while start < len(line):
            while start < len(line) and line[start].isspace():
                start += 1
             
            if start >= len(line):
                break
               
            if line[start].isdigit():
                startIndex = start

                while start < len(line) and line[start].isdigit():
                    start += 1
   
                words.append(line[startIndex : start])
            elif line[start].isalpha(): 
                startIndex = start

                while start < len(line) and line[start].isalpha():
                    start += 1
   
                words.append(line[startIndex : start].lower())
            else:
                words.append(line[start])
                start += 1
            
    return words
