import math

class EvaluationMeasures(object):

    #J=TP/N-TN
    #TP=((sum(sum(n^2))-n)/2
    #TN=[n^2-sum(n^2)-sum(m^2)+sum(sum(n^2))]/2
    def Jaccard(self,matrix,i):
        n=300 #number of elements
        squareSum=0


        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                squareSum+=matrix[row][col]**2

        TP = (squareSum - n) / 2
        TN=0

        if i<4:
            sumT = self.sumT(matrix)
            sumC=self.sumC(matrix)
            for row in matrix:
                for val in row:
                    print ('{:3}'.format(val)),
                print
            TN= (n**2-(sumC[0]**2+sumC[1]**2+sumC[2]**2)-(sumT[0]**2+sumT[1]**2+sumT[2]**2) + squareSum)/2
            print ('T:' + str(sumT[0])+','+str(sumT[1])+','+str(sumT[2]))
            print ('C:' + str(sumC[0]) + ',' + str(sumC[1]) + ',' + str(sumC[2]))

        if i ==4:
            sum5T = self.sum5T(matrix)
            sum5C = self.sum5C(matrix)
            TN = (n ** 2 - (sum5C[0] ** 2 + sum5C[1] ** 2 + sum5C[2] ** 2+ sum5C[3] ** 2+ sum5C[4] ** 2) - (
                    sum5T[0] ** 2 + sum5T[1] ** 2 + sum5T[2] ** 2) + squareSum)/2

        if i == 5:
            sum2T = self.sum2T(matrix)
            sum2C = self.sum2C(matrix)
            TN = (n ** 2 - (sum2C[0] ** 2 + sum2C[1] ** 2) - (
                    sum2T[0] ** 2 + sum2T[1] ** 2 + sum2T[2] ** 2) + squareSum)/2

        return TP/(n-TN)

    def sumC(self, matrix):
        sumC1 = matrix[0][0] + matrix[1][0] + matrix[2][0]
        sumC2 = matrix[0][1] + matrix[1][1] + matrix[2][1]
        sumC3 = matrix[0][2] + matrix[1][2] + matrix[2][2]
        
        return (sumC1,sumC2,sumC3)
    
    def sumT(self, matrix):
        sumT1 = matrix[0][0] + matrix[0][1] + matrix[0][2]
        sumT2 = matrix[1][0] + matrix[1][1] + matrix[1][2]
        sumT3 = matrix[2][0] + matrix[2][1] + matrix[2][2]
        
        return (sumT1,sumT2,sumT3)

    def sum2T(self, matrix):
        sumT1 = matrix[0][0] + matrix[0][1]
        sumT2 = matrix[1][0] + matrix[1][1]
        sumT3 = matrix[2][0] + matrix[2][1]

        return (sumT1, sumT2,sumT3)

    def sum5T(self, matrix):
        sumT1 = matrix[0][0] + matrix[0][1] + matrix[0][2] +matrix[0][3] + matrix[0][4]
        sumT2 = matrix[1][0] + matrix[1][1] + matrix[1][2]+ matrix[1][3] + matrix[1][4]
        sumT3 = matrix[2][0] + matrix[2][1] + matrix[2][2]+ matrix[2][3] + matrix[2][4]

        return (sumT1, sumT2, sumT3)

    def sum2C(self, matrix):
        sumC1 = matrix[0][0] + matrix[1][0] + matrix[2][0]
        sumC2 = matrix[0][1] + matrix[1][1] + matrix[2][1]

        return (sumC1, sumC2)

    def sum5C(self, matrix):
        sumC1 = matrix[0][0] + matrix[1][0] + matrix[2][0]
        sumC2 = matrix[0][1] + matrix[1][1] + matrix[2][1]
        sumC3 = matrix[0][2] + matrix[1][2] + matrix[2][2]
        sumC4 = matrix[0][3] + matrix[1][3] + matrix[2][3]
        sumC5 = matrix[0][4] + matrix[1][4] + matrix[2][4]

        return (sumC1, sumC2, sumC3,sumC4, sumC5)
    
    def NMI(self,matrix,i):
        sumT=0
        sumC=0
        if i<4:
            sumT=self.sumT(matrix)
            sumC=self.sumC(matrix)

        if i==4:
            sumT = self.sum5T(matrix)
            sumC = self.sum5C(matrix)
        if i == 5:
            sumT = self.sum2T(matrix)
            sumC = self.sum2C(matrix)

        totalSum=sum(sumC)
        HC=self.H(sumC)
        HT=self.H(sumT)
        I=self.I(matrix,totalSum,sumT,sumC)
        NMI=I/math.sqrt(HC*HT)
        return NMI

    def I(self,matrix,totalSum,sumT,sumC):
        I=0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                pij=matrix[i][j]/totalSum
                if pij==0:
                    continue
                pti=sumT[i]/totalSum
                if pti==0:
                    continue
                pci=sumC[j]/totalSum
                if pci==0:
                    continue
                I+=pij*math.log(pij/(pti*pci),2)
        return I
        
    def H(self, sums):
        totalSum=sum(sums)
        h=0
        for item in sums:
            p=item/totalSum
            h+=-p*math.log(p,2)
        
        return h
