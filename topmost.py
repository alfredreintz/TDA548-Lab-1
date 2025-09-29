import wordfreq
import sys
import urllib.request

def main():
    fullTextFileOpen = False

    # Get inputs from the terminal
    stopWords = open(sys.argv[1], encoding="utf-8")


    response = urllib.request.urlopen(sys.argv[2])
    # If the second argument starts with a http request the text is imported from the desired website
    if sys.argv[2].startswith("http://") or sys.argv[2].startswith("https://"):
        fullText = response.read().decode("utf8").splitlines()
    else:
        fullText = open(sys.argv[2], encoding="utf-8")
        fullTextFileOpen = True

    outputCount = int(sys.argv[3])

    # Create a list and add elements by stripping away new line symboles
    splitStopWords = []
    for line in stopWords:
        stripLine = line.strip("\n")
        splitStopWords.append(stripLine)

    splitFullText = wordfreq.tokenize(fullText)
    countedWords = wordfreq.countWords(splitFullText, splitStopWords)

    wordfreq.printTopMost(countedWords, outputCount)

    stopWords.close()
    if fullTextFileOpen: fullText.close()

main()