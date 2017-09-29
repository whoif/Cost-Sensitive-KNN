from numpy import *

def mat2file(fn, mat):
    with open(fn,'w') as fp:
        size=mat.shape
        for i in range(0,size[0]):
            for j in range(0,size[1]):
                fp.write(str(mat[i][j]))
                fp.write(' ')
            fp.write('\n')


def file2mat(fn, de=' '):
    arr = []
    with open(fn) as fr:
        for line in fr:
            tLine = line.strip().split(de)
            arr.append(tLine)
    return array(arr)
