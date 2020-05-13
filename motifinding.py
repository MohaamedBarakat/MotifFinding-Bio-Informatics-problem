#t  -   number of sample DNA sequences
#n  -   length of each DNA sequence
#DNA - sample of DNA sequences (t x n array)
#l  -   length of the motif 
from itertools import product
class Motifs :
    def __init__(self,t,n,l,DNA):
        self.t = t
        self.n = n
        self.DNA = DNA
        self.dicOf = {'A' : 0 ,'C': 0 , 'T' : 0 ,'G' : 0}
        self.bestConsequenceString = None
        self.bestSeqInd = None
        self.bestscore = 0
        pass
    def HamminDistance(self,fSeq,sSeq):
        dis = 0
        for index in range(len(fSeq)):
            if fSeq[index] != sSeq[index]:
                dis+=1
        return dis
    def best_Score(self,dna,seqList,seqLen):
        def helpBestScore(dna,seqList,seqLen):
            aligment = []
            for index in seqList :
                aligment.append(dna[index : index + seqLen])
            return aligment

        tempDic = {}
        aligment = helpBestScore(dna,seqList,seqLen)
        for column in range(0,seqLen) :
            for index in range(len(aligment)):
                self.dicOf[aligment[index][column]]+=1
            tempDic[column] = self.dicOf
            self.dicOf['A'],self.dicOf['C'],self.dicOf['T'],self.dicOf['G'] = 0 , 0 , 0 , 0
        
        totalScore = 0
        maxVal = 0
        maxKey = None
        conseq = ''
        for col in tempDic :
            for key,val in col.item():
                if val >= maxVal :
                    maxVal = val
                    maxKey = key
            totalScore+=maxVal
            conseq += maxKey 

        if self.bestscore <= totalScore :
            self.bestscore = totalScore
            self.bestConsequence = conseq
            self.bestSeqInd = seqList

    def getConsequencString(self,l,n):
        StartingPostionList = list(product([i for i in range(n-l+1)], repeat=l))
        for seqList in StartingPostionList :
            self.best_Score(self.DNA,seqList,l)
        return self.bestConsequenceString

        

        



            


