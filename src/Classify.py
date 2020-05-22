#Author: Ori Weiss
#Version: 1.0
from sklearn.neighbors import KNeighborsClassifier
import math

def findShortestDistance(array, outputSize):
    result = [0] * outputSize
    for i in range(len(array)):
        curr = array[i]
        inserted = False
        j = 0
        while(j < len(result) and not inserted):
            if(curr < array[result[j]]):
                result.insert(j,i)
                if len(result) >= outputSize:
                    result.pop(outputSize)
                inserted = True
            j+=1
    return result


def KNNClassifier(features,labels, predictionSet, nNeigbors):
    #setup the array
    distances = [[0 for x in range(len(features))] for y in range(len(predictionSet))]

    #find all distances
    for i in range(len(predictionSet)):
        for j in range(len(features)):
            distances[i][j] = math.sqrt(math.pow(predictionSet[i][0] - features[j][0], 2) +
                                        math.pow(predictionSet[i][1] - features[j][1], 2) +
                                        math.pow(predictionSet[i][2] - features[j][2], 2)
                                        )
    result = [0] * len(predictionSet)
    for i in range(len(distances)):
        shortestDistances = findShortestDistance(distances[i],nNeigbors)
        healthy = 0
        sickle = 0
        for j in range(len(shortestDistances)):
            if labels[shortestDistances[j]] == 0:
                healthy += 1
            elif  labels[shortestDistances[j]] == 1:
                sickle += 1
        if healthy > sickle:
            result[i] = 0
        elif sickle > healthy:
            result[i] = 1

    return result

