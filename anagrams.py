
###O(n^2) quadratic time
def anagramSolution1(s1, s2):
    stillOk = True
    if len(s1) != len(s2):
        stillOk = False

    alist = list(s2)
    pos1 = 0

    while pos1 < len(s1) and stillOk:
        pos2 = 0
        found = False
        while pos2 < len(alist) and not found:
            if s1[pos1] == alist[pos2]:
                found = True
            else:
                pos2 = pos2 + 1

        if found:
            alist[pos2] == None

        else:
            stillOk = False
        
        pos1 = pos1 + 1

    return stillOk

###O(n^2) or O(n log n) sorting operations dominate the iteration --> this algo will have the same order of magnitude as that of the sorting process
def anagramSolution2(s1, s2):
    alist1 = list(s1)
    alist2 = list(s2)

    alist1.sort()
    alist2.sort()

    pos = 0
    matches = True

    while pos < len(s1) and matches:
        if alist1[pos] == alist2[pos]:
            pos = pos + 1
        else:
            matches = False 

    return matches


        


