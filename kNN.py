import fileHelper as fh
import plotHelper as ph
from numpy import *
from alg import *


def getCostMat():
    return array([[0, 10], [1, 0]])


def getCostVec():
    return array([3, 5])


def getData(dataFilename, size=100, genNew=False, override=False):
    try:
        if genNew:
            raise BaseException
        inp = fh.file2mat(dataFilename)
        inp = array([[int(numeric_string) for numeric_string in row] for row in inp])
    except:
        inp = array([[random.randint(0, 1001) for _ in range(2)] for _ in range(size)])
        if not genNew or override:
            fh.mat2file(dataFilename, inp)
    labels = [None] * inp.shape[0]
    for i in range(inp.shape[0]):
        if inp[i][0] >= 600 and inp[i][1] >= 600:
            labels[i] = 1
        else:
            labels[i] = 0
    return inp, array(labels)


def judge(answer, truth, costMat=None):
    err = 0
    for i in range(answer.size):
        if costMat is None:
            err = err + 1
        else:
            err = err + costMat[truth[i]][answer[i]]
    return err, where(answer != truth)[0]


data, label = getData('data.txt', 200, genNew=True)
testSet, truth = getData('test.txt', 200, genNew=True)

answer = kNN(testSet, data, label, 5)
err, fInd = judge(answer, truth, getCostMat())
print(err)
tInd = array([i for i in range(testSet.shape[0]) if i not in fInd])
ph.p2d2cls(data, label, testSet[tInd], truth[tInd], testSet[fInd], answer[fInd], False)

answer = csKNN(testSet, data, label, 5, getCostVec())
err, fInd = judge(answer, truth, getCostMat())
print(err)
tInd = array([i for i in range(testSet.shape[0]) if i not in fInd])
ph.p2d2cls(data, label, testSet[tInd], truth[tInd], testSet[fInd], answer[fInd])
