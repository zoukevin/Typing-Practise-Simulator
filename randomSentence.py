from random import randrange

def getRandomWord(fileName, n):
    randNoun = randrange(n)
    with open(fileName) as fp:
        for i, line in enumerate(fp):
            if i == randNoun:
                return line.strip()

def getRandomSentence():
    sentence = ""

    numNouns = 1525
    numVerbs = 1011
    numAdverbs = 255
    numAdjectives = 527

    sentence += getRandomWord("adjectives.txt", numAdjectives).title() + " "
    sentence += getRandomWord("nouns.txt", numNouns) + " "
    sentence += getRandomWord("verbs.txt", numVerbs) + "s "
    sentence += getRandomWord("adjectives.txt", numAdjectives) + " "
    sentence += getRandomWord("nouns.txt", numNouns) + " "
    sentence += getRandomWord("adverbs.txt", numAdverbs) + "."
    return(sentence)



    