from IOHandler import *
from EvaluationMeasures import *
import numpy as np

def main():
    io = IOHandler()
    partitions = io.readFromFile('partitions.txt')
    em = EvaluationMeasures()
    for i in range(1,6):
        file= 'clustering_{}.txt'.format(i)
        clusters = io.readFromFile(file)

        matrix=constructContingencyMatrix(clusters,partitions,i)
        nmi = em.NMI(matrix, i)
        jaccard=em.Jaccard(matrix,i)


        io.writeToFile("scores.txt",nmi,jaccard)


def constructContingencyMatrix(clusters,partitions,i):

    contingency_matrix = np.zeros((3, 3))  # hardcoded for now
    if i == 4:
        contingency_matrix = np.zeros((3, 5))  # hardcoded for now
    if i == 5:
        contingency_matrix = np.zeros((3, 2))  # hardcoded for now
    for i in range(len(clusters)):
        contingency_matrix[partitions[i]][clusters[i]] += 1

    return contingency_matrix

if __name__=="__main__":
    main()