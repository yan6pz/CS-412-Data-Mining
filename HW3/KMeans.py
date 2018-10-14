from math import radians, cos, sin, sqrt,asin
import random
from IOHandler import *
import copy

class KMeans(object):

    def __init__(self, numClusters,maxNum):
        self.numClusters = numClusters
        self.numClustersFixed=numClusters
        self.MAX_NUM=maxNum
        self.minLatitude = 30
        self.maxLatitude = 45
        self.minLongitude = -115
        self.maxLongitude = -80
        self.clusters = {}
        self.initialAssignClusterCenters()



    def reassignObjectToCluster(self,data):
        for point in data:
            self.assignPointToItsClosestCluster(point)

        print data

    def assignPointToItsClosestCluster(self,point):
        minDistance=1e30000
        for key, value in self.clusters.iteritems():
            distance = self.haversine(point.lat,point.lng,value.lat,value.lng)
            if distance < minDistance:
                minDistance=distance
                clusterToAssign=key

        point.clusterKey=clusterToAssign
        print point

    def haversine(self, lon1, lat1, lon2, lat2):
        lon1, lat1, lon2, lat2 = map(float, [lon1, lat1, lon2, lat2])
        lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
        c = 2 * asin(sqrt(a))
        meter = 6371 * c * 1000
        return meter

    def updateClusterCenters(self, data):
        for key, value in self.clusters.iteritems():
            pointsInCluster = [num for num in data if num.clusterKey ==key]
            if len(pointsInCluster)==0:
                continue
            meanLatitude=sum(float(x.lat) for x in pointsInCluster) / float(len(pointsInCluster))
            meanLongitude = sum(float(x.lng) for x in pointsInCluster) / float(len(pointsInCluster))
            value.lat=meanLatitude
            value.lng=meanLongitude


    def initialAssignClusterCenters(self):
        while self.numClusters>0:
            self.clusters[self.numClusters]=Point(random.uniform(self.minLongitude,self.maxLongitude),random.uniform(self.minLatitude,self.maxLatitude),self.numClusters)
            self.numClusters-=1

    '''
    def assignClusterCentersBasedOnData(self,data):
        while self.numClusters > 0:
            self.numClusters -= 1
            pointsInCluster=[]
            for item in range(0,len(data)):
                if item % self.numClustersFixed == self.numClusters:
                    pointsInCluster.append(data[item])
            meanpart_lat=sum(float(x.lat) for x in pointsInCluster) / float(len(pointsInCluster))
            meanpart_lng = sum(float(x.lng) for x in pointsInCluster) / float(len(pointsInCluster))
            self.clusters[self.numClusters] = Point(meanpart_lat,
                                                    meanpart_lng,
                                                    self.numClusters)
    '''


    def clusterNotConverged(self,previousClusters):
        for item in range(1, self.numClustersFixed):
            if self.clusters[item].lat!=previousClusters[item].lat or self.clusters[item].lng!=previousClusters[item].lng:
                return True
        return False

    def stopCriteria(self,iteration,previousClusters):
        if iteration>self.MAX_NUM:
            return False
        return self.clusterNotConverged(previousClusters)

    def main(self):
        io=IOHandler()
        data=io.readFromFile('places.txt')
        iteration=0
        previousClusters = copy.deepcopy(self.clusters)
        while self.stopCriteria(iteration,previousClusters) or iteration==0:
            self.reassignObjectToCluster(data)
            self.updateClusterCenters(data)
            iteration=iteration+1

        io.writeToFile("clusters.txt",data,None)

    def assignLabels(self):
        io = IOHandler()
        data = io.readFromFile('places.txt')
        io.writeToFile("places1.txt", data,1)









