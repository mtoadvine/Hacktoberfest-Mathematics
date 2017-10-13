## Calculate the number of possible subsets of a larger set.
## 
## combin calculates the Combination and perm for the Permutation
## permRep calculates the permutation where items are not removed each time
## permWithout calculates the permutation where items are removed each time
##
## nItems - Number of items to choose from
## nChoose - Number of items chosen from the items available

def combin(nItems, nChoose):
    #Returns the Combination
    #Order doesn't matter
    nN = fact(nItems)
    nR = fact(nChoose)
    nDiff = fact(nItems - nChoose)

    nComb = nN/(nR * nDiff)

    return nComb

def permRep(nItems, nChoose):
    #Returns the permutation with repetition
    #Order does matter
    nPerm = nItems ** nChoose
    return nPerm

def permWithout(nItems, nChoose):
    #Returns the Permutation without repetition
    #Order does matter
    nNum = fact(nItems)
    nDom = fact(nItems - nChoose)

    nPerm = nNum/nDom
    return nPerm



def fact(nItems):
    #Gives the factorial for nItems
    #Commonly denoted n!
    nPerm = 1
    for nCount in range(1,nItems + 1):
        nPerm = nPerm * nCount
    return nPerm


