import wordfreq
import sys

stopWords = open(sys.argv[1], encoding="utf-8")
fullText = open(sys.argv[2], encoding="utf-8")
outputCount = sys.argv[3]

splitStopWords = wordfreq.tokenize(stopWords)
splitFullText = wordfreq.tokenize(fullText)

countedWords = wordfreq.countWords(splitFullText, splitStopWords)

wordfreq.printTopMost(countedWords, outputCount)