
class IOHandler(object):

    def __init__ (self):
        print ('initialize')

    def readFromFile(self,name):
        points=[]
        with open(name) as fp:
            line = fp.readline()
            cnt = 1
            while line:
                coordinates=line.strip('\n').split(' ')
                points.append(int(coordinates[1]))
                line = fp.readline()
                cnt += 1
        return points

    def writeToFile(self,name,nmi,jaccard):
        pointNumber=0
        with open(name, 'a') as output:
            output.write('{} {}\n'.format( nmi,jaccard))
            pointNumber+=1

        return True
