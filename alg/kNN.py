from numpy import *

__all__ = ['kNN', 'csKNN']


def doKNN(testSet, dataSet, label, k, costVec=None):
    answer = [None] * testSet.shape[0]
    for i in range(testSet.shape[0]):
        x = testSet[i]
        dataSize = dataSet.shape[0]
        tiled = tile(x, [dataSize, 1])
        sqDiffMat = (tiled - dataSet) ** 2
        sqSumDiff = sqDiffMat.sum(axis=1)
        if costVec is not None:
            sqSumDiff = sqSumDiff * array([costVec[label[i]] for i in range(label.size)])
        ind = sqSumDiff.argsort()
        classCount = {}
        for j in range(k):
            vote = label[ind[j]]
            classCount[vote] = classCount.get(vote, 0) + 1
        answer[i] = max(classCount, key=classCount.get)
    return array(answer)


def kNN(testSet, dataSet, label, k):
    return doKNN(testSet, dataSet, label, k)


def csKNN(testSet, dataSet, label, k, costVec):
    return doKNN(testSet, dataSet, label, k, costVec)
