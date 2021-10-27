import os
import json

specification = open('codepoints.json', 'r')
specs = json.load(specification)

spec_version = "1.0";

def transmit(words):
    #Checks if the function input is an array of words
    typeCheck1 = isinstance(words, list)
    typeCheck2 = False
    wordslength = 0
    if typeCheck1 == True & len(words) != 0 :
        wordslength = len(words)
        typeCheck2 = True
        iteration = 0
        while iteration < wordslength & typeCheck2 == True:
            if isinstance(words[iteration],str) == False:
                typeCheck2 = False
            iteration += 1    
    if typeCheck2 == True & typeCheck1 == True:
        internalTramsit(words)
    else:
        print("Format incorrect. Please input a list of strings.")

def internalTramsit(words):
    #Counts the Amount of Letters in the message to make sure there is no more than 2
    #Checks if all the words inputted are valid.
    letterCount = 0
    wordsValid = True
    #insert while loop that checks every word in the message to see if a a non-null value is outputted. If it is, wordsValid is set to false, ending the loop, and an error is returned.
    iteration = 0
    while iteration < len(words) and wordsValid == True:
        if getWordNumber(words[iteration]) == None :
            wordsValid = False
        iteration += 1 
    if wordsValid == True:
        #Insert while loop that counts either until the end of words array or when letterCount gets to 2
        iteration = 0
        while letterCount < 3 or iteration < len(words) :
            if getWordType(words[iteration]) == "Letters" :
                letterCount += 1
            iteration += 1
        if letterCount < 3:
            message = []
            for i in words:
                message.append("{\"version\": "+spec_version+", \"Code\": "+str(getWordNumber(i))+"}")
            print(message)
        else:
            print("Error. Too many characters of type letter.")
    else:
        print("Error. Message has invalid words")
    
def getWordType(word):
    if isinstance(word,str) == True:
        codeN = None
        iteration = 0
        while codeN == None or iteration < len(specs) :
            if specs[iteration]['Meaning'] == word:
                codeN = specs[iteration]['Type']
            iteration += 1
        return codeN
    else:
        print('String Value Required')

def getWordNumber(word):
    if isinstance(word,str) == True:
        codeN = None
        iteration = 0
        while codeN == None or iteration < len(specs) :
            if specs[iteration]['Meaning'] == word:
                codeN = specs[iteration]['Code']
            iteration += 1
        return codeN
    else:
        print('String Value Required')

internalTramsit(["Red", "Z", "A"])