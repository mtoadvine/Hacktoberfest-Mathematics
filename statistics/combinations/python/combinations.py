## Calculate the number of possible subsets of a larger set when order doesn't matter.
##
## nItems - Number of items to choose from
## nChoose - Number of items chosen from the items available

def choose(nItems, nChoose):

    nN = fact(nItems)
    nR = fact(nChoose)
    nDiff = fact(nItems - nChoose)

    nComb = nN/(nR * nDiff)

    return nComb 


def fact(nItems):
    #Gives the factorial for nItems
    #Commonly denoted n!
    nPerm = 1
    for nCount in range(1,nItems + 1):
        nPerm = nPerm * nCount
    return nPerm





