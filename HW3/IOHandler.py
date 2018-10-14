from Point import Point
class IOHandler(object):

    def __init__ (self):
        print 'initialize'

    def readFromFile(self,name):
        points=[]
        with open(name) as fp:
            line = fp.readline()
            cnt = 1
            while line:
                coordinates=line.strip('\n').split(',')
                points.append(Point(coordinates[0],coordinates[1]))
                line = fp.readline()
                cnt += 1
        return points

    def writeToFile(self,name,points, label):
        pointNumber=0
        with open(name, 'a') as output:
            while pointNumber<len(points):
                if label is not None:
                    output.write('{},{},{}\n'.format(pointNumber, points[pointNumber].lng,points[pointNumber].lat))
                else:
                    output.write('{} {}\n'.format(pointNumber, points[pointNumber].clusterKey-1))
                pointNumber+=1

        return True