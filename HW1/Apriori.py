# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 11:19:49 2018

@author: Yanis
"""

class Apriori:
    """
    Data format:
    { [a1,a2,a3]: support,[a4,a5,a6]: support}
    """
    hashTableScan= {}

    def apriori_prop_infreq_subset(self, arrK, itemSets):
        """
        Remove all k item sets for which at least one from the k-1 itemsets
        in not frequent
        """
        arr = generate_kminus1_items(arrK,len(itemSets[0]))
        for item in arr:
            if item in itemSets:
                del itemSet[item]
        return True
    
      def apriori_prune(self, itemSet, minsup):
        for item in itemSet :
            if itemSet[item] < minsup:
                del itemSet[item]
        return True
    
      def data_scan(self,fileName):
        f = open(fileName,"r") 
        for line in f.readlines():
            items = line.split(";")
            for item in items:
                hashTableScan[item]++
        
        f.close()
        return True
    
    def apriori_gen(self, itemSets):
        newHash={}
        
        for i, key in enumerate(itemSets):
            for j, key1 in enumerate(itemSets):
                k=0
                arrI=itemSets[i]
                arrJ=itemSets[j]
                k_count=0
                for k, val in enumerate(arrI): 
                    if arrI[k]!=arrJ[k]:
                        break
                    k_count+=1
                if k_count < len(arrI): #if first k-1 items are same merge and k-th is different merge the two sequences
                    continue
                if arrI[k]<arrJ[k]:
                    arrK=generate_combinations(arrI,arrJ)
                    if !apriori_prop_infreq_subset(arrK,itemSets):
                        newHash[arrK]=0
          return newHash  
        
        
    def main(self):
        
    
    if __name__ == "__main__":
        main()
