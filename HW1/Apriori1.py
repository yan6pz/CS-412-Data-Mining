# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 14:31:56 2018

@author: Yanis
"""

from collections import defaultdict # iterable


def returnItemsWithMinSupport(itemSet, transactionList, minSupport, freqSet):
        """calculates the support for items in the itemSet and returns a subset
       of the itemSet each of whose elements satisfies the minimum support"""
        _itemSet = set()
        localSet = defaultdict(int)

        # checking whether the generated set is part of any of the transaction sets
        for item in itemSet:
                for transaction in transactionList:
                        if item.issubset(transaction): #transaction list
                                freqSet[item] += 1
                                localSet[item] += 1

        for item, absSupport in localSet.items():
                if absSupport >= minSupport * len(transactionList):
                        _itemSet.add(item)

        return _itemSet


def joinSet(itemSet, length):
        """Join a set with itself and returns the n-element itemsets"""
        return set([i.union(j) for i in itemSet for j in itemSet if len(i.union(j)) == length])


def getItemSetTransactionList(data_iterator):
    transactionList = list()
    itemSet = set()
    for record in data_iterator:
        transaction = frozenset(record)#frozenset to be hashable
        transactionList.append(transaction) # len = the number of transactions
        for item in transaction:
            itemSet.add(frozenset([item])) # Generate 1-itemSets
    return itemSet, transactionList


def runApriori(data_iter, minSupport):
    """
    run the apriori algorithm. data_iter is a record iterator
    Return both:
     - items (tuple, support)
     - rules ((pretuple, posttuple), confidence)
    """
    itemSet, transactionList = getItemSetTransactionList(data_iter)

    freqSet = defaultdict(int)
        # Global dictionary which stores (key=n-itemSets,value=support)
    # which satisfy minSupport
    largeSet = dict()

    oneCSet = returnItemsWithMinSupport(itemSet,
                                        transactionList,
                                        minSupport,
                                        freqSet)

    currentLSet = oneCSet
    k = 2
    #until there are no more LSets satisfying the min support threshold we generate new 
    # k+1 super sets
    while(currentLSet != set([])):
        largeSet[k-1] = currentLSet
        currentLSet = joinSet(currentLSet, k)
        currentCSet = returnItemsWithMinSupport(currentLSet,
                                                transactionList,
                                                minSupport,
                                                freqSet)
        currentLSet = currentCSet
        k = k + 1

    def getRelativeSupport(item):
            """local function which Returns the support of an item"""
            return float(freqSet[item])/len(transactionList)
        
    def getAbsoluteSupport(item):
            """local function which Returns the support of an item"""
            return freqSet[item]

    toRetItems = []
    for key, value in largeSet.items():
        toRetItems.extend([(tuple(item), getAbsoluteSupport(item))
                           for item in value])

    return toRetItems


def saveResults(items):
    file = open('patterns.txt','w') 
 
    for item in items:
        file.write("%.d:%s\n" % (item[1],';'.join(map(str, item[0])))) 
    file.close() 


def dataFromFile(fname):
        """Function which reads from the file and yields a generator"""
        file_iter = open(fname, 'r')
        for line in file_iter:
                line = line.strip().rstrip(';')                         # Remove trailing comma
                record = frozenset(line.split(';'))
                yield record


if __name__ == "__main__":

    inFile = dataFromFile("categories.txt")
    minSupport =0.01 

    items = runApriori(inFile, minSupport)
    saveResults(items)