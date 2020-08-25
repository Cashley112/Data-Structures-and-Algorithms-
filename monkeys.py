import random

def generateOne(str_len):
    alphabet = 'abcdefghijklmnopqrstuvwxyz '
    res = ''
    for i in range(str_len):
        res = res + alphabet[random.randrange(27)]

    return res

def score(goal, teststring):
    numSame = 0
    for i in range(len(goal)):
        if goal[i] == teststring[i]:
            numSame = numSame + 1
    return numSame / len(goal)




def main():

    goalstring = 'methinks it is like a weasel'
    newstring = generateOne(28)
    best = 0
    newscore = score(goalstring, newstring)
    main_tracker = 0
    while newscore < 1:
        if newscore >= best:
            best = newscore
        newstring = generateOne(28)
        newscore = score(goalstring, newstring)
        main_tracker = main_tracker + 1
        

main()





