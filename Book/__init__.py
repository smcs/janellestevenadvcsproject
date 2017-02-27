#!/usr/bin/env python
import nltk
nltk.download()
from nltk import FreqDist
from PyDictionary import PyDictionary
dictionary = PyDictionary()

searchlist = ["good", "sweet"]


for listword in range(len(searchlist)):
    word = searchlist[listword]  # the word we're looking for (including synonyms)
    wordcount = 0  # how many instances of the word
    wordlist = []  # what synonyms we found

# open up the book!
    sample = open("Loadbook.txt")
    linecount = 0
# walk through the book, line by line
    for line in sample:
        linecount = linecount + 1  #counts the line number
    # is our search term in the line?

        if word in line:
            if word not in wordlist:
                wordlist.append(word)
            print(line)
            wordcount = wordcount + line.count(word)
            print("Occurs on line " + str(linecount))
        for w in dictionary.synonym(word):
            if w in line:
                if w not in wordlist:
                    wordlist.append(w)
                    print(line)
                    wordcount = wordcount + line.count(w)
                    print("Occurs on line " + str(linecount))

                fdist1 = FreqDist(sample)
                fdist1
                vocabulary1 = fdist1.keys()
                vocabulary1[:50]
# print out the results
print("There are {} Occurrences like {} ({})".format(wordcount, word, wordlist))


