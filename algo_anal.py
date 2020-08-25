import time
from random import randrange

def sumOfN(n):
    start = time.time()

    theSum = 0
    for i in range(1, n+1):
        theSum = theSum + i

    end = time.time()

    return theSum, end - start

def sumOfN3(n):
    

    return (n*(n+1))/2

def findMin(alist):
    overallmin = alist[0]
    for i in alist:
        issmallest = True
        for j in alist:
            if i > j:
                issmallest = False
        if issmallest:
            overallmin = i

    return overallmin
    
def findMin(alist):
    minsofar = alist[0]
    for i in alist:
        if i < minsofar:
            minsofar = i

    return minsofar


for listSize in range(1000, 100001, 1000):
    alist = [randrange(100000) for x in range(listSize)]
    start = time.time()
    print(findMin(alist))
    end = time.time()
    print('size: %d time: %f' % (listSize, end-start))


