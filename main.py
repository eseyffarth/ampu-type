__author__ = 'Esther Seyffarth'

def sortwords(wordlist, lefthand, righthand):
    leftwords = set()
    rightwords = set()
    for word in wordlist:
        word = word.strip()
        if word[0].lower() in lefthand:
            if check_leftness(word, lefthand):
                leftwords.add(word)
        elif word[0].lower() in righthand:
            if check_rightness(word, righthand):
                rightwords.add(word)
    return leftwords, rightwords

def check_leftness(word, lefthand):
    for character in word:
        if not character.lower() in lefthand:
            return False
    return True

def check_rightness(word, righthand):
    for character in word:
        if not character.lower() in righthand:
            return False
    return True

def pretty_output(leftwords, rightwords):
    right_outfile = open("rightwords.txt", "w")
    left_outfile = open("leftwords.txt", "w")
    for item in sorted(leftwords, key=len, reverse=True):
        if len(item) > 3:
            print(item, file = left_outfile)
    for item in sorted(rightwords, key=len, reverse=True):
        if len(item) > 3:
            print(item, file = right_outfile)
    print("Your words have been written to the hard drive")


lefthand = "qwertsadfgyxcvb"
righthand = "zuiopühjklöänm-"
wordlist = open("D:/Korpora/german.dic", "r").readlines()

leftwords, rightwords = sortwords(wordlist, lefthand, righthand)
pretty_output(leftwords, rightwords)